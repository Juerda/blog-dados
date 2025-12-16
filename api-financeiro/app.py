from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import jwt
import os
from functools import wraps

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": ["*"]}})

# Configurações
database_url = os.getenv('DATABASE_URL', 'sqlite:///financeiro.db')
# Vercel Postgres usa postgres:// mas SQLAlchemy precisa de postgresql://
if database_url.startswith('postgres://'):
    database_url = database_url.replace('postgres://', 'postgresql://', 1)

app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')

db = SQLAlchemy(app)

# Modelos
class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    last_login = db.Column(db.DateTime)
    
    transactions = db.relationship('Transaction', backref='user', lazy=True, cascade='all, delete-orphan')
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'created_at': self.created_at.isoformat(),
            'last_login': self.last_login.isoformat() if self.last_login else None
        }

class Transaction(db.Model):
    __tablename__ = 'transactions'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    external_id = db.Column(db.String(100), index=True)  # FITID do OFX
    date = db.Column(db.Date, nullable=False, index=True)
    description = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(50), nullable=False, index=True)
    amount = db.Column(db.Float, nullable=False)
    transaction_type = db.Column(db.String(20))  # DEBIT, CREDIT, OTHER
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'external_id': self.external_id,
            'date': self.date.isoformat(),
            'description': self.description,
            'category': self.category,
            'amount': self.amount,
            'type': self.transaction_type
        }

# Decorador de autenticação
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        
        if not token:
            return jsonify({'error': 'Token ausente'}), 401
        
        try:
            if token.startswith('Bearer '):
                token = token[7:]
            
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = User.query.get(data['user_id'])
            
            if not current_user:
                return jsonify({'error': 'Usuário não encontrado'}), 401
                
        except jwt.ExpiredSignatureError:
            return jsonify({'error': 'Token expirado'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Token inválido'}), 401
        
        return f(current_user, *args, **kwargs)
    
    return decorated

# Rotas de Autenticação
@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    
    # Validações
    if not data.get('name') or not data.get('email') or not data.get('password'):
        return jsonify({'error': 'Nome, email e senha são obrigatórios'}), 400
    
    if len(data['password']) < 6:
        return jsonify({'error': 'Senha deve ter no mínimo 6 caracteres'}), 400
    
    # Verificar se email já existe
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'error': 'Email já cadastrado'}), 409
    
    # Criar usuário
    user = User(
        name=data['name'],
        email=data['email'],
        password_hash=generate_password_hash(data['password'])
    )
    
    db.session.add(user)
    db.session.commit()
    
    return jsonify({
        'message': 'Usuário criado com sucesso',
        'user': user.to_dict()
    }), 201

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    
    if not data.get('email') or not data.get('password'):
        return jsonify({'error': 'Email e senha são obrigatórios'}), 400
    
    user = User.query.filter_by(email=data['email']).first()
    
    if not user or not check_password_hash(user.password_hash, data['password']):
        return jsonify({'error': 'Email ou senha incorretos'}), 401
    
    # Atualizar último login
    user.last_login = datetime.utcnow()
    db.session.commit()
    
    # Gerar token JWT (válido por 7 dias)
    token = jwt.encode({
        'user_id': user.id,
        'exp': datetime.utcnow() + timedelta(days=7)
    }, app.config['SECRET_KEY'], algorithm='HS256')
    
    return jsonify({
        'token': token,
        'user': user.to_dict()
    }), 200

@app.route('/api/me', methods=['GET'])
@token_required
def get_current_user(current_user):
    return jsonify(current_user.to_dict()), 200

# Rotas de Transações
@app.route('/api/transactions', methods=['GET'])
@token_required
def get_transactions(current_user):
    transactions = Transaction.query.filter_by(user_id=current_user.id).order_by(Transaction.date.desc()).all()
    return jsonify([t.to_dict() for t in transactions]), 200

@app.route('/api/transactions', methods=['POST'])
@token_required
def create_transaction(current_user):
    data = request.get_json()
    
    # Validações
    required_fields = ['date', 'description', 'category', 'amount']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Campos obrigatórios faltando'}), 400
    
    # Verificar duplicata por external_id (FITID)
    if data.get('external_id'):
        existing = Transaction.query.filter_by(
            user_id=current_user.id,
            external_id=data['external_id']
        ).first()
        
        if existing:
            return jsonify({'error': 'Transação duplicada', 'transaction': existing.to_dict()}), 409
    
    transaction = Transaction(
        user_id=current_user.id,
        external_id=data.get('external_id'),
        date=datetime.fromisoformat(data['date'].replace('Z', '+00:00')).date(),
        description=data['description'],
        category=data['category'],
        amount=float(data['amount']),
        transaction_type=data.get('type', 'OTHER')
    )
    
    db.session.add(transaction)
    db.session.commit()
    
    return jsonify(transaction.to_dict()), 201

@app.route('/api/transactions/bulk', methods=['POST'])
@token_required
def create_transactions_bulk(current_user):
    data = request.get_json()
    transactions_data = data.get('transactions', [])
    
    created = []
    skipped = []
    
    for t_data in transactions_data:
        # Verificar duplicata
        if t_data.get('external_id'):
            existing = Transaction.query.filter_by(
                user_id=current_user.id,
                external_id=t_data['external_id']
            ).first()
            
            if existing:
                skipped.append(t_data['external_id'])
                continue
        
        transaction = Transaction(
            user_id=current_user.id,
            external_id=t_data.get('external_id'),
            date=datetime.fromisoformat(t_data['date'].replace('Z', '+00:00')).date(),
            description=t_data['description'],
            category=t_data['category'],
            amount=float(t_data['amount']),
            transaction_type=t_data.get('type', 'OTHER')
        )
        
        db.session.add(transaction)
        created.append(transaction)
    
    db.session.commit()
    
    return jsonify({
        'created': len(created),
        'skipped': len(skipped),
        'transactions': [t.to_dict() for t in created]
    }), 201

@app.route('/api/transactions/<int:transaction_id>', methods=['PUT'])
@token_required
def update_transaction(current_user, transaction_id):
    transaction = Transaction.query.filter_by(id=transaction_id, user_id=current_user.id).first()
    
    if not transaction:
        return jsonify({'error': 'Transação não encontrada'}), 404
    
    data = request.get_json()
    
    if 'date' in data:
        transaction.date = datetime.fromisoformat(data['date'].replace('Z', '+00:00')).date()
    if 'description' in data:
        transaction.description = data['description']
    if 'category' in data:
        transaction.category = data['category']
    if 'amount' in data:
        transaction.amount = float(data['amount'])
    if 'type' in data:
        transaction.transaction_type = data['type']
    
    db.session.commit()
    
    return jsonify(transaction.to_dict()), 200

@app.route('/api/transactions/<int:transaction_id>', methods=['DELETE'])
@token_required
def delete_transaction(current_user, transaction_id):
    transaction = Transaction.query.filter_by(id=transaction_id, user_id=current_user.id).first()
    
    if not transaction:
        return jsonify({'error': 'Transação não encontrada'}), 404
    
    db.session.delete(transaction)
    db.session.commit()
    
    return jsonify({'message': 'Transação excluída com sucesso'}), 200

@app.route('/api/transactions/clear', methods=['DELETE'])
@token_required
def clear_transactions(current_user):
    Transaction.query.filter_by(user_id=current_user.id).delete()
    db.session.commit()
    
    return jsonify({'message': 'Todas as transações foram removidas'}), 200

# Rotas administrativas
@app.route('/api/admin/users', methods=['GET'])
def get_all_users():
    # Em produção, adicionar autenticação admin
    users = User.query.all()
    return jsonify([u.to_dict() for u in users]), 200

@app.route('/api/admin/stats', methods=['GET'])
def get_stats():
    # Em produção, adicionar autenticação admin
    total_users = User.query.count()
    total_transactions = Transaction.query.count()
    
    return jsonify({
        'total_users': total_users,
        'total_transactions': total_transactions
    }), 200

# Inicialização
@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok', 'message': 'API Financeiro funcionando'}), 200

@app.route('/', methods=['GET'])
def index():
    return jsonify({
        'name': 'API Financeiro',
        'version': '1.0.0',
        'endpoints': [
            '/api/health',
            '/api/register',
            '/api/login',
            '/api/me',
            '/api/transactions',
            '/api/admin/users',
            '/api/admin/stats'
        ]
    }), 200

# Criar tabelas automaticamente
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True, port=5000)
