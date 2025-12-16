# API Financeiro - Backend

API REST para o Dashboard Financeiro com autenticação JWT e banco de dados.

## 🚀 Tecnologias

- **Flask** - Framework web Python
- **SQLAlchemy** - ORM para banco de dados
- **PostgreSQL/SQLite** - Banco de dados
- **JWT** - Autenticação via tokens
- **Flask-CORS** - Suporte a requisições cross-origin

## 📋 Estrutura do Banco de Dados

### Tabela `users`
- `id` - Integer, Primary Key
- `name` - String(100), Nome completo
- `email` - String(120), Unique, Email do usuário
- `password_hash` - String(255), Senha criptografada
- `created_at` - DateTime, Data de criação
- `updated_at` - DateTime, Última atualização
- `last_login` - DateTime, Último login

### Tabela `transactions`
- `id` - Integer, Primary Key
- `user_id` - Integer, Foreign Key → users.id
- `external_id` - String(100), FITID do OFX
- `date` - Date, Data da transação
- `description` - String(255), Descrição
- `category` - String(50), Categoria
- `amount` - Float, Valor (negativo para despesas)
- `transaction_type` - String(20), Tipo (DEBIT/CREDIT/OTHER)
- `created_at` - DateTime, Data de criação
- `updated_at` - DateTime, Última atualização

## 🔧 Instalação

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Instalar dependências
pip install -r requirements.txt

# Configurar variáveis de ambiente
cp .env.example .env
# Editar .env com suas configurações

# Executar API
python app.py
```

A API estará disponível em `http://localhost:5000`

## 📡 Endpoints

### Autenticação

**POST /api/register**
```json
{
  "name": "João Silva",
  "email": "joao@email.com",
  "password": "senha123"
}
```

**POST /api/login**
```json
{
  "email": "joao@email.com",
  "password": "senha123"
}
```
Retorna: `{ "token": "...", "user": {...} }`

**GET /api/me**
Headers: `Authorization: Bearer <token>`

### Transações

**GET /api/transactions**
Headers: `Authorization: Bearer <token>`

**POST /api/transactions**
Headers: `Authorization: Bearer <token>`
```json
{
  "date": "2025-12-16",
  "description": "Supermercado",
  "category": "Alimentação",
  "amount": -150.50,
  "type": "DEBIT",
  "external_id": "12345" // opcional
}
```

**POST /api/transactions/bulk**
Headers: `Authorization: Bearer <token>`
```json
{
  "transactions": [
    { "date": "...", "description": "...", ... },
    { "date": "...", "description": "...", ... }
  ]
}
```

**PUT /api/transactions/<id>**
Headers: `Authorization: Bearer <token>`

**DELETE /api/transactions/<id>**
Headers: `Authorization: Bearer <token>`

**DELETE /api/transactions/clear**
Headers: `Authorization: Bearer <token>`

### Admin

**GET /api/admin/users** - Lista todos os usuários

**GET /api/admin/stats** - Estatísticas gerais

**GET /api/health** - Status da API

## 🗄️ Banco de Dados

### SQLite (Desenvolvimento)
```env
DATABASE_URL=sqlite:///financeiro.db
```

### PostgreSQL (Produção)
```env
DATABASE_URL=postgresql://user:password@localhost/financeiro
```

## 🔐 Segurança

- ✅ Senhas criptografadas com Werkzeug
- ✅ Tokens JWT com expiração de 7 dias
- ✅ Validação de duplicatas (FITID)
- ✅ Isolamento de dados por usuário
- ✅ CORS configurado

## 🚀 Deploy

### Vercel (Recomendado para API Python)

1. Instalar Vercel CLI:
```bash
npm i -g vercel
```

2. Criar `vercel.json`:
```json
{
  "version": 2,
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app.py"
    }
  ]
}
```

3. Deploy:
```bash
vercel --prod
```

### Render.com

1. Criar conta em render.com
2. Conectar repositório GitHub
3. Configurar:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
4. Adicionar variáveis de ambiente

## 📊 Consultas SQL Úteis

```sql
-- Total de usuários
SELECT COUNT(*) FROM users;

-- Transações por usuário
SELECT u.name, COUNT(t.id) as total_transactions
FROM users u
LEFT JOIN transactions t ON t.user_id = u.id
GROUP BY u.id;

-- Gastos por categoria
SELECT category, SUM(amount) as total
FROM transactions
WHERE user_id = 1 AND amount < 0
GROUP BY category
ORDER BY total;
```

## 🧪 Testes

```bash
# Testar registro
curl -X POST http://localhost:5000/api/register \
  -H "Content-Type: application/json" \
  -d '{"name":"Test","email":"test@test.com","password":"123456"}'

# Testar login
curl -X POST http://localhost:5000/api/login \
  -H "Content-Type: application/json" \
  -d '{"email":"test@test.com","password":"123456"}'

# Testar transações
curl -X GET http://localhost:5000/api/transactions \
  -H "Authorization: Bearer <seu-token>"
```

## 📝 Licença

MIT
