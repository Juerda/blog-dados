Title: Dashboard Financeiro
Date: 2025-12-16
Slug: dashboard
Summary: Gerencie suas finanças pessoais - Adicione, edite e importe transações OFX

<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">

<div id="financial-dashboard">
    <style>
        * {
            box-sizing: border-box;
        }
        
        .dashboard-container {
            max-width: 100%;
            width: 100%;
            margin: 0 auto;
            padding: 1rem;
            overflow-x: hidden;
        }
        
        .dashboard-header {
            text-align: center;
            margin-bottom: 2rem;
        }
        
        .dashboard-header h1 {
            font-size: clamp(1.5rem, 4vw, 2.5rem);
            color: var(--primary-blue);
            margin-bottom: 0.5rem;
        }
        
        .dashboard-header p {
            font-size: clamp(0.9rem, 2vw, 1.1rem);
            color: var(--text-secondary);
        }
        
        .actions-bar {
            display: flex;
            gap: 1rem;
            margin-bottom: 2rem;
            flex-wrap: wrap;
            justify-content: center;
        }
        
        .btn {
            padding: 0.75rem 1.5rem;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-weight: 600;
            transition: all 0.3s;
            font-size: 0.95rem;
        }
        
        .btn-primary {
            background: var(--primary-blue);
            color: white;
        }
        
        .btn-success {
            background: #10b981;
            color: white;
        }
        
        .btn-danger {
            background: #ef4444;
            color: white;
        }
        
        .btn-secondary {
            background: #6b7280;
            color: white;
        }
        
        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
        }
        
        .metrics-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            margin-bottom: 2rem;
            width: 100%;
        }
        
        .metric-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 1.25rem;
            border-radius: 12px;
            color: white;
            text-align: center;
            min-width: 0;
        }
        
        .metric-card.income {
            background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        }
        
        .metric-card.expense {
            background: linear-gradient(135deg, #eb3349 0%, #f45c43 100%);
        }
        
        .metric-card.balance {
            background: linear-gradient(135deg, #4776e6 0%, #8e54e9 100%);
        }
        
        .metric-label {
            font-size: 0.9rem;
            opacity: 0.9;
            margin-bottom: 0.5rem;
        }
        
        .metric-value {
            font-size: clamp(1.3rem, 3vw, 2rem);
            font-weight: bold;
            word-break: break-word;
        }
        
        .charts-section {
            margin-bottom: 2rem;
            width: 100%;
        }
        
        .chart-card {
            background: var(--bg-secondary);
            padding: 1.5rem;
            border-radius: 12px;
            border: 1px solid var(--border-color);
            margin-bottom: 1.5rem;
            width: 100%;
        }
        
        .chart-card h3 {
            margin-top: 0;
            margin-bottom: 1rem;
            color: var(--text-primary);
            font-size: clamp(1rem, 2.5vw, 1.25rem);
        }
        
        .chart-card canvas {
            max-width: 100%;
            height: auto !important;
        }
        
        .transactions-section {
            background: var(--bg-secondary);
            padding: 1.5rem;
            border-radius: 12px;
            border: 1px solid var(--border-color);
            width: 100%;
            overflow: hidden;
        }
        
        .transactions-section h3 {
            margin-top: 0;
            font-size: clamp(1rem, 2.5vw, 1.25rem);
        }
        
        .filters {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            margin-bottom: 1.5rem;
        }
        
        .filter-group {
            min-width: 0;
        }
        
        .filter-group label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: 600;
            color: var(--text-primary);
            font-size: 0.9rem;
        }
        
        .filter-group select,
        .filter-group input {
            width: 100%;
            padding: 0.5rem;
            border: 1px solid var(--border-color);
            border-radius: 6px;
            background: var(--bg-primary);
            color: var(--text-primary);
            font-size: 0.9rem;
        }
        
        .table-container {
            width: 100%;
            overflow-x: auto;
            -webkit-overflow-scrolling: touch;
        }
        
        .transactions-table {
            width: 100%;
            border-collapse: collapse;
            min-width: 600px;
        }
        
        .transactions-table thead {
            background: var(--bg-primary);
            position: sticky;
            top: 0;
            z-index: 10;
        }
        
        .transactions-table th,
        .transactions-table td {
            padding: 0.75rem;
            text-align: left;
            border-bottom: 1px solid var(--border-color);
            font-size: 0.9rem;
        }
        
        .transactions-table th {
            font-weight: 600;
            color: var(--text-primary);
            white-space: nowrap;
        }
        
        .transactions-table tbody tr:hover {
            background: var(--bg-primary);
        }
        
        .amount-positive {
            color: #10b981;
            font-weight: 600;
        }
        
        .amount-negative {
            color: #ef4444;
            font-weight: 600;
        }
        
        .category-badge {
            display: inline-block;
            padding: 0.25rem 0.75rem;
            border-radius: 12px;
            font-size: 0.8rem;
            background: var(--primary-blue);
            color: white;
            white-space: nowrap;
        }
        
        .action-buttons {
            display: flex;
            gap: 0.5rem;
        }
        
        .btn-sm {
            padding: 0.25rem 0.75rem;
            font-size: 0.8rem;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            transition: all 0.2s;
        }
        
        .btn-edit {
            background: #3b82f6;
            color: white;
        }
        
        .btn-delete {
            background: #ef4444;
            color: white;
        }
        
        .btn-sm:hover {
            opacity: 0.8;
        }
        
        /* Modal */
        .modal {
            display: none;
            position: fixed;
            z-index: 1000;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.5);
            overflow-y: auto;
        }
        
        .modal.active {
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        .modal-content {
            background-color: var(--bg-primary);
            margin: 1rem;
            padding: 2rem;
            border: 1px solid var(--border-color);
            border-radius: 12px;
            width: 90%;
            max-width: 500px;
            max-height: 90vh;
            overflow-y: auto;
        }
        
        .modal-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1.5rem;
        }
        
        .modal-header h2 {
            margin: 0;
            color: var(--text-primary);
            font-size: 1.5rem;
        }
        
        .close-modal {
            font-size: 2rem;
            font-weight: bold;
            color: var(--text-secondary);
            cursor: pointer;
            border: none;
            background: none;
            padding: 0;
            line-height: 1;
        }
        
        .close-modal:hover {
            color: var(--text-primary);
        }
        
        .form-group {
            margin-bottom: 1rem;
        }
        
        .form-group label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: 600;
            color: var(--text-primary);
        }
        
        .form-group input,
        .form-group select,
        .form-group textarea {
            width: 100%;
            padding: 0.75rem;
            border: 1px solid var(--border-color);
            border-radius: 6px;
            background: var(--bg-secondary);
            color: var(--text-primary);
            font-size: 1rem;
        }
        
        .form-group textarea {
            resize: vertical;
            min-height: 80px;
        }
        
        .loading {
            text-align: center;
            padding: 2rem;
            color: var(--text-secondary);
        }
        
        .loading-spinner {
            border: 3px solid var(--border-color);
            border-top-color: var(--primary-blue);
            border-radius: 50%;
            width: 40px;
            height: 40px;
            animation: spin 1s linear infinite;
            margin: 0 auto 1rem;
        }
        
        @keyframes spin {
            to { transform: rotate(360deg); }
        }
        
        .error-message {
            background: #fee;
            color: #c00;
            padding: 1rem;
            border-radius: 8px;
            margin-bottom: 1rem;
        }
        
        .success-message {
            background: #d4edda;
            color: #155724;
            padding: 1rem;
            border-radius: 8px;
            margin-bottom: 1rem;
        }
        
        .empty-state {
            text-align: center;
            padding: 3rem 1rem;
            color: var(--text-secondary);
        }
        
        .empty-state-icon {
            font-size: 4rem;
            margin-bottom: 1rem;
        }
        
        /* Auth Screen */
        #authScreen {
            display: flex;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 1rem;
        }
        
        .auth-container {
            background: var(--bg-primary);
            border-radius: 16px;
            padding: 2rem;
            width: 100%;
            max-width: 400px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
        }
        
        .auth-header {
            text-align: center;
            margin-bottom: 2rem;
        }
        
        .auth-header h1 {
            font-size: 2rem;
            color: var(--primary-blue);
            margin-bottom: 0.5rem;
        }
        
        .auth-header p {
            color: var(--text-secondary);
            font-size: 0.95rem;
        }
        
        .auth-form {
            display: flex;
            flex-direction: column;
            gap: 1rem;
        }
        
        .auth-toggle {
            text-align: center;
            margin-top: 1.5rem;
            color: var(--text-secondary);
        }
        
        .auth-toggle button {
            background: none;
            border: none;
            color: var(--primary-blue);
            text-decoration: underline;
            cursor: pointer;
            font-weight: 600;
        }
        
        .auth-toggle button:hover {
            color: #0056b3;
        }
        
        #dashboardScreen {
            display: none;
        }
        
        .user-info {
            display: flex;
            align-items: center;
            gap: 1rem;
            margin-bottom: 1rem;
            padding: 0.75rem;
            background: var(--bg-secondary);
            border-radius: 8px;
        }
        
        .user-info span {
            font-weight: 600;
            color: var(--text-primary);
        }
        
        .user-info button {
            margin-left: auto;
        }
        
        /* Responsividade */
        @media (max-width: 1200px) {
            .dashboard-container {
                padding: 1rem;
            }
            
            .metrics-grid {
                grid-template-columns: repeat(2, 1fr);
            }
        }
        
        @media (max-width: 768px) {
            .dashboard-container {
                padding: 0.5rem;
            }
            
            .actions-bar {
                flex-direction: column;
            }
            
            .btn {
                width: 100%;
            }
            
            .metrics-grid {
                grid-template-columns: 1fr 1fr;
                gap: 0.75rem;
            }
            
            .metric-card {
                padding: 1rem;
            }
            
            .filters {
                grid-template-columns: 1fr;
            }
            
            .transactions-table th,
            .transactions-table td {
                padding: 0.5rem 0.25rem;
                font-size: 0.8rem;
            }
            
            .modal-content {
                padding: 1.5rem 1rem;
            }
        }
        
        @media (max-width: 480px) {
            .metrics-grid {
                grid-template-columns: 1fr;
            }
            
            .action-buttons {
                flex-direction: column;
            }
            
            .btn-sm {
                width: 100%;
            }
        }
    </style>
    
    <!-- Tela de Autenticação -->
    <div id="authScreen">
        <div class="auth-container">
            <div class="auth-header">
                <h1>💰 Dashboard Financeiro</h1>
                <p>Gerencie suas finanças pessoais</p>
            </div>
            
            <!-- Formulário de Login -->
            <form id="loginForm" class="auth-form" onsubmit="handleLogin(event)">
                <div class="form-group">
                    <label>Email</label>
                    <input type="email" id="loginEmail" required placeholder="seu@email.com" />
                </div>
                
                <div class="form-group">
                    <label>Senha</label>
                    <input type="password" id="loginPassword" required placeholder="••••••" />
                </div>
                
                <button type="submit" class="btn btn-primary" style="width: 100%;">Entrar</button>
                
                <div class="auth-toggle">
                    Não tem conta? <button type="button" onclick="switchToRegister()">Cadastre-se</button>
                </div>
            </form>
            
            <!-- Formulário de Cadastro -->
            <form id="registerForm" class="auth-form" style="display: none;" onsubmit="handleRegister(event)">
                <div class="form-group">
                    <label>Nome Completo</label>
                    <input type="text" id="registerName" required placeholder="Seu nome" />
                </div>
                
                <div class="form-group">
                    <label>Email</label>
                    <input type="email" id="registerEmail" required placeholder="seu@email.com" />
                </div>
                
                <div class="form-group">
                    <label>Senha (mín. 6 caracteres)</label>
                    <input type="password" id="registerPassword" required placeholder="••••••" minlength="6" />
                </div>
                
                <div class="form-group">
                    <label>Confirmar Senha</label>
                    <input type="password" id="registerConfirmPassword" required placeholder="••••••" minlength="6" />
                </div>
                
                <button type="submit" class="btn btn-success" style="width: 100%;">Criar Conta</button>
                
                <div class="auth-toggle">
                    Já tem conta? <button type="button" onclick="switchToLogin()">Fazer login</button>
                </div>
            </form>
        </div>
    </div>
    
    <!-- Tela do Dashboard -->
    <div id="dashboardScreen">
    <div class="dashboard-container">
        <div class="dashboard-header">
            <h1>💰 Dashboard Financeiro Pessoal</h1>
            <p>Gerencie suas finanças - Adicione, edite e importe transações</p>
        </div>
        
        <div class="user-info">
            <span>👤 <span id="userNameDisplay"></span></span>
            <button class="btn btn-danger btn-sm" onclick="logout()">🚪 Sair</button>
        </div>
        
        <div class="actions-bar">
            <button class="btn btn-success" onclick="openAddModal()">➕ Nova Transação</button>
            <button class="btn btn-primary" onclick="openImportModal()">📁 Importar OFX</button>
            <button class="btn btn-secondary" onclick="exportToCSV()">📥 Exportar CSV</button>
            <button class="btn btn-danger" onclick="clearAllData()">🗑️ Limpar Tudo</button>
        </div>
        
        <div id="messageSection"></div>
        
        <div id="dashboardContent">
            <div class="metrics-grid">
                <div class="metric-card income">
                    <div class="metric-label">💰 Receitas</div>
                    <div class="metric-value" id="totalIncome">R$ 0,00</div>
                </div>
                <div class="metric-card expense">
                    <div class="metric-label">💸 Despesas</div>
                    <div class="metric-value" id="totalExpenses">R$ 0,00</div>
                </div>
                <div class="metric-card balance">
                    <div class="metric-label">💵 Saldo</div>
                    <div class="metric-value" id="netBalance">R$ 0,00</div>
                </div>
                <div class="metric-card">
                    <div class="metric-label">📝 Transações</div>
                    <div class="metric-value" id="totalTransactions">0</div>
                </div>
            </div>
            
            <div class="charts-section">
                <div class="chart-card">
                    <h3>📊 Despesas por Categoria</h3>
                    <canvas id="categoryChart"></canvas>
                </div>
                <div class="chart-card">
                    <h3>📈 Tendência Mensal</h3>
                    <canvas id="monthlyChart"></canvas>
                </div>
            </div>
            
            <div class="transactions-section">
                <h3>📋 Transações</h3>
                
                <div class="filters">
                    <div class="filter-group">
                        <label>Categoria</label>
                        <select id="categoryFilter" onchange="applyFilters()">
                            <option value="">Todas</option>
                        </select>
                    </div>
                    <div class="filter-group">
                        <label>Tipo</label>
                        <select id="typeFilter" onchange="applyFilters()">
                            <option value="">Todas</option>
                            <option value="income">Receitas</option>
                            <option value="expense">Despesas</option>
                        </select>
                    </div>
                    <div class="filter-group">
                        <label>Buscar</label>
                        <input type="text" id="searchFilter" placeholder="Buscar descrição..." oninput="applyFilters()" />
                    </div>
                </div>
                
                <div class="table-container">
                    <table class="transactions-table">
                        <thead>
                            <tr>
                                <th>Data</th>
                                <th>Descrição</th>
                                <th>Categoria</th>
                                <th>Valor</th>
                                <th>Ações</th>
                            </tr>
                        </thead>
                        <tbody id="transactionsBody"></tbody>
                    </table>
                </div>
                
                <div id="emptyState" class="empty-state" style="display: none;">
                    <div class="empty-state-icon">📊</div>
                    <h3>Nenhuma transação cadastrada</h3>
                    <p>Comece adicionando uma transação manualmente ou importe um arquivo OFX</p>
                </div>
            </div>
        </div>
    </div>
    </div>
    
    <!-- Modal Adicionar/Editar -->
    <div id="transactionModal" class="modal">
        <div class="modal-content">
            <div class="modal-header">
                <h2 id="modalTitle">Nova Transação</h2>
                <button class="close-modal" onclick="closeModal()">&times;</button>
            </div>
            <form id="transactionForm" onsubmit="saveTransaction(event)">
                <input type="hidden" id="transactionId" />
                
                <div class="form-group">
                    <label>Data *</label>
                    <input type="date" id="transactionDate" required />
                </div>
                
                <div class="form-group">
                    <label>Descrição *</label>
                    <input type="text" id="transactionDescription" required placeholder="Ex: Supermercado" />
                </div>
                
                <div class="form-group">
                    <label>Categoria *</label>
                    <select id="transactionCategory" required>
                        <option value="">Selecione...</option>
                        <option value="Alimentação">Alimentação</option>
                        <option value="Transporte">Transporte</option>
                        <option value="Moradia">Moradia</option>
                        <option value="Saúde">Saúde</option>
                        <option value="Educação">Educação</option>
                        <option value="Lazer">Lazer</option>
                        <option value="Vestuário">Vestuário</option>
                        <option value="Serviços">Serviços</option>
                        <option value="Investimentos">Investimentos</option>
                        <option value="Receitas">Receitas</option>
                        <option value="Transferências">Transferências</option>
                        <option value="Outros">Outros</option>
                    </select>
                </div>
                
                <div class="form-group">
                    <label>Valor (R$) *</label>
                    <input type="number" id="transactionAmount" step="0.01" required placeholder="0.00" />
                </div>
                
                <div class="form-group">
                    <label>Tipo *</label>
                    <select id="transactionType" required>
                        <option value="expense">Despesa (-)</option>
                        <option value="income">Receita (+)</option>
                    </select>
                </div>
                
                <div style="display: flex; gap: 1rem; margin-top: 1.5rem;">
                    <button type="submit" class="btn btn-success" style="flex: 1;">Salvar</button>
                    <button type="button" class="btn btn-secondary" onclick="closeModal()" style="flex: 1;">Cancelar</button>
                </div>
            </form>
        </div>
    </div>
    
    <!-- Modal Importar OFX -->
    <div id="importModal" class="modal">
        <div class="modal-content">
            <div class="modal-header">
                <h2>Importar Arquivo OFX</h2>
                <button class="close-modal" onclick="closeImportModal()">&times;</button>
            </div>
            <div>
                <p style="margin-bottom: 1rem; color: var(--text-secondary);">
                    As transações do arquivo OFX serão <strong>adicionadas</strong> às existentes. 
                    Transações duplicadas serão ignoradas.
                </p>
                
                <div class="form-group">
                    <input type="file" id="ofxFile" accept=".ofx,.OFX" style="width: 100%;" />
                </div>
                
                <div id="importLoading" class="loading" style="display: none;">
                    <div class="loading-spinner"></div>
                    <p>Processando arquivo OFX...</p>
                </div>
                
                <div style="display: flex; gap: 1rem; margin-top: 1.5rem;">
                    <button class="btn btn-primary" onclick="processOFXFile()" style="flex: 1;">Importar</button>
                    <button class="btn btn-secondary" onclick="closeImportModal()" style="flex: 1;">Cancelar</button>
                </div>
            </div>
        </div>
    </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>

<script>
// Configuração da API
// IMPORTANTE: Após fazer deploy da API, substitua pela URL da sua API na Vercel
// Exemplo: const API_URL = 'https://api-financeiro-seu-usuario.vercel.app/api';
const API_URL = window.location.hostname === 'localhost' 
    ? 'http://localhost:5000/api'
    : 'https://api-financeiro.vercel.app/api'; // TROCAR PELA SUA URL
let authToken = null;

// Variáveis globais
let transactionsData = [];
let currentUser = null;
let charts = {
    category: null,
    monthly: null
};

// Categorias
const CATEGORIES = {
    'Alimentação': ['supermercado', 'restaurante', 'lanchonete', 'padaria', 'ifood', 'uber eats'],
    'Transporte': ['uber', '99', 'combustível', 'gasolina', 'estacionamento', 'taxi'],
    'Moradia': ['aluguel', 'condomínio', 'iptu', 'água', 'luz', 'energia', 'internet'],
    'Saúde': ['farmácia', 'médico', 'hospital', 'plano de saúde', 'dentista'],
    'Educação': ['escola', 'faculdade', 'curso', 'livro'],
    'Lazer': ['cinema', 'netflix', 'spotify', 'academia', 'viagem'],
    'Vestuário': ['roupa', 'calçado', 'loja'],
    'Serviços': ['cabeleireiro', 'barbeiro', 'lavanderia'],
    'Investimentos': ['aplicação', 'poupança', 'cdb', 'ações'],
    'Receitas': ['salário', 'freelance', 'venda', 'rendimento'],
    'Transferências': ['pix', 'ted', 'doc', 'transferência'],
    'Outros': []
};

// LocalStorage
function saveAuthToken(token) {
    authToken = token;
    localStorage.setItem('authToken', token);
}

function loadAuthToken() {
    authToken = localStorage.getItem('authToken');
    return authToken;
}

function clearAuthToken() {
    authToken = null;
    localStorage.removeItem('authToken');
}

// API Helper
async function apiRequest(endpoint, options = {}) {
    const config = {
        headers: {
            'Content-Type': 'application/json',
            ...options.headers
        },
        ...options
    };
    
    if (authToken && !options.skipAuth) {
        config.headers['Authorization'] = `Bearer ${authToken}`;
    }
    
    try {
        const response = await fetch(`${API_URL}${endpoint}`, config);
        const data = await response.json();
        
        if (!response.ok) {
            if (response.status === 401) {
                clearAuthToken();
                showAuthScreen();
                showMessage('Sessão expirada. Faça login novamente.', 'error');
            }
            throw new Error(data.error || 'Erro na requisição');
        }
        
        return data;
    } catch (error) {
        console.error('API Error:', error);
        throw error;
    }
}

// Carregar transações do servidor
async function loadFromServer() {
    try {
        const data = await apiRequest('/transactions');
        transactionsData = data.map(t => ({
            ...t,
            date: new Date(t.date)
        }));
    } catch (error) {
        showMessage('Erro ao carregar transações: ' + error.message, 'error');
        transactionsData = [];
    }
}

// Autenticação
async function register(name, email, password) {
    try {
        const data = await apiRequest('/register', {
            method: 'POST',
            body: JSON.stringify({ name, email, password }),
            skipAuth: true
        });
        
        showMessage(data.message, 'success');
        return true;
    } catch (error) {
        showMessage(error.message, 'error');
        return false;
    }
}

async function login(email, password) {
    try {
        const data = await apiRequest('/login', {
            method: 'POST',
            body: JSON.stringify({ email, password }),
            skipAuth: true
        });
        
        saveAuthToken(data.token);
        currentUser = data.user;
        showMessage(`Bem-vindo(a), ${data.user.name}!`, 'success');
        return true;
    } catch (error) {
        showMessage(error.message, 'error');
        return false;
    }
}

async function logout() {
    if (confirm('Deseja realmente sair?')) {
        clearAuthToken();
        currentUser = null;
        transactionsData = [];
        showAuthScreen();
        showMessage('Logout realizado com sucesso', 'success');
    }
}

async function checkAuth() {
    const token = loadAuthToken();
    if (!token) return false;
    
    try {
        const data = await apiRequest('/me');
        currentUser = data;
        return true;
    } catch (error) {
        clearAuthToken();
        return false;
    }
}

function showAuthScreen() {
    document.getElementById('authScreen').style.display = 'flex';
    document.getElementById('dashboardScreen').style.display = 'none';
}

function showDashboardScreen() {
    document.getElementById('authScreen').style.display = 'none';
    document.getElementById('dashboardScreen').style.display = 'block';
    document.getElementById('userNameDisplay').textContent = currentUser.name;
}

function switchToRegister() {
    document.getElementById('loginForm').style.display = 'none';
    document.getElementById('registerForm').style.display = 'block';
}

function switchToLogin() {
    document.getElementById('registerForm').style.display = 'none';
    document.getElementById('loginForm').style.display = 'block';
}

async function handleLogin(event) {
    event.preventDefault();
    const email = document.getElementById('loginEmail').value;
    const password = document.getElementById('loginPassword').value;
    
    if (await login(email, password)) {
        await loadFromServer();
        showDashboardScreen();
        renderDashboard();
    }
}

async function handleRegister(event) {
    event.preventDefault();
    const name = document.getElementById('registerName').value;
    const email = document.getElementById('registerEmail').value;
    const password = document.getElementById('registerPassword').value;
    const confirmPassword = document.getElementById('registerConfirmPassword').value;
    
    if (password !== confirmPassword) {
        showMessage('As senhas não coincidem', 'error');
        return;
    }
    
    if (await register(name, email, password)) {
        document.getElementById('registerForm').reset();
        switchToLogin();
    }
}

// Inicialização
document.addEventListener('DOMContentLoaded', async function() {
    if (await checkAuth()) {
        await loadFromServer();
        showDashboardScreen();
        renderDashboard();
    } else {
        showAuthScreen();
    }
});

// Modais
function openAddModal() {
    document.getElementById('modalTitle').textContent = 'Nova Transação';
    document.getElementById('transactionForm').reset();
    document.getElementById('transactionId').value = '';
    document.getElementById('transactionDate').valueAsDate = new Date();
    document.getElementById('transactionModal').classList.add('active');
}

function openEditModal(id) {
    const transaction = transactionsData.find(t => t.id === id);
    if (!transaction) return;
    
    document.getElementById('modalTitle').textContent = 'Editar Transação';
    document.getElementById('transactionId').value = transaction.id;
    document.getElementById('transactionDate').valueAsDate = transaction.date;
    document.getElementById('transactionDescription').value = transaction.description;
    document.getElementById('transactionCategory').value = transaction.category;
    document.getElementById('transactionAmount').value = Math.abs(transaction.amount);
    document.getElementById('transactionType').value = transaction.amount >= 0 ? 'income' : 'expense';
    document.getElementById('transactionModal').classList.add('active');
}

function closeModal() {
    document.getElementById('transactionModal').classList.remove('active');
}

function openImportModal() {
    document.getElementById('importModal').classList.add('active');
    document.getElementById('ofxFile').value = '';
}

function closeImportModal() {
    document.getElementById('importModal').classList.remove('active');
}

// CRUD Transações
async function saveTransaction(event) {
    event.preventDefault();
    
    const id = document.getElementById('transactionId').value;
    const date = new Date(document.getElementById('transactionDate').value);
    const description = document.getElementById('transactionDescription').value;
    const category = document.getElementById('transactionCategory').value;
    let amount = parseFloat(document.getElementById('transactionAmount').value);
    const type = document.getElementById('transactionType').value;
    
    if (type === 'expense' && amount > 0) amount = -amount;
    if (type === 'income' && amount < 0) amount = Math.abs(amount);
    
    try {
        if (id) {
            // Editar
            await apiRequest(`/transactions/${id}`, {
                method: 'PUT',
                body: JSON.stringify({
                    date: date.toISOString(),
                    description,
                    category,
                    amount,
                    type: type === 'income' ? 'CREDIT' : 'DEBIT'
                })
            });
            showMessage('Transação atualizada com sucesso!', 'success');
        } else {
            // Adicionar
            await apiRequest('/transactions', {
                method: 'POST',
                body: JSON.stringify({
                    date: date.toISOString(),
                    description,
                    category,
                    amount,
                    type: type === 'income' ? 'CREDIT' : 'DEBIT'
                })
            });
            showMessage('Transação adicionada com sucesso!', 'success');
        }
        
        await loadFromServer();
        renderDashboard();
        closeModal();
    } catch (error) {
        showMessage('Erro ao salvar: ' + error.message, 'error');
    }
}

async function deleteTransaction(id) {
    if (!confirm('Tem certeza que deseja excluir esta transação?')) return;
    
    try {
        await apiRequest(`/transactions/${id}`, { method: 'DELETE' });
        await loadFromServer();
        renderDashboard();
        showMessage('Transação excluída com sucesso!', 'success');
    } catch (error) {
        showMessage('Erro ao excluir: ' + error.message, 'error');
    }
}

async function clearAllData() {
    if (!confirm('Tem certeza que deseja limpar TODAS as transações? Esta ação não pode ser desfeita!')) return;
    
    try {
        await apiRequest('/transactions/clear', { method: 'DELETE' });
        await loadFromServer();
        renderDashboard();
        showMessage('Todas as transações foram removidas!', 'success');
    } catch (error) {
        showMessage('Erro ao limpar dados: ' + error.message, 'error');
    }
}

// Importar OFX
async function processOFXFile() {
    const fileInput = document.getElementById('ofxFile');
    const file = fileInput.files[0];
    
    if (!file) {
        showMessage('Selecione um arquivo OFX', 'error');
        return;
    }
    
    document.getElementById('importLoading').style.display = 'block';
    
    const reader = new FileReader();
    reader.onload = async function(e) {
        try {
            const ofxData = e.target.result;
            const newTransactions = parseOFX(ofxData);
            
            // Enviar em lote para API
            const result = await apiRequest('/transactions/bulk', {
                method: 'POST',
                body: JSON.stringify({ transactions: newTransactions })
            });
            
            await loadFromServer();
            renderDashboard();
            closeImportModal();
            showMessage(`${result.created} transações importadas com sucesso!`, 'success');
            
        } catch (error) {
            showMessage('Erro ao processar arquivo OFX: ' + error.message, 'error');
        } finally {
            document.getElementById('importLoading').style.display = 'none';
        }
    };
    reader.readAsText(file);
}

function parseOFX(ofxText) {
    const transactions = [];
    
    try {
        const stmttrnPattern = /<STMTTRN>([\s\S]*?)<\/STMTTRN>/g;
        const matches = ofxText.matchAll(stmttrnPattern);
        
        for (const match of matches) {
            const trnBlock = match[1];
            
            const dtposted = trnBlock.match(/<DTPOSTED>(\d+)/)?.[1];
            const trnamt = trnBlock.match(/<TRNAMT>([-\d.]+)/)?.[1];
            const fitid = trnBlock.match(/<FITID>([^<]+)/)?.[1];
            const memo = trnBlock.match(/<MEMO>([^<]*)/)?.[1] || '';
            const name = trnBlock.match(/<NAME>([^<]*)/)?.[1] || '';
            const trntype = trnBlock.match(/<TRNTYPE>([^<]+)/)?.[1];
            
            if (!dtposted || !trnamt) continue;
            
            const year = parseInt(dtposted.substring(0, 4));
            const month = parseInt(dtposted.substring(4, 6)) - 1;
            const day = parseInt(dtposted.substring(6, 8));
            
            let description = memo || name || 'Sem descrição';
            description = description.trim().replace(/^["']|["']$/g, '');
            
            const amount = parseFloat(trnamt);
            const category = autoCategorize(description, amount);
            
            transactions.push({
                date: new Date(year, month, day).toISOString(),
                description: description,
                amount: amount,
                type: trntype || 'OTHER',
                external_id: fitid || Date.now().toString() + Math.random(),
                category: category
            });
        }
        
        return transactions.sort((a, b) => new Date(b.date) - new Date(a.date));
        
    } catch (error) {
        console.error('Erro ao processar OFX:', error);
        throw new Error('Erro ao processar arquivo OFX');
    }
}

function autoCategorize(description, amount) {
    const desc = description.toLowerCase();
    
    if (amount > 0) return 'Receitas';
    
    for (const [category, keywords] of Object.entries(CATEGORIES)) {
        for (const keyword of keywords) {
            if (desc.includes(keyword)) return category;
        }
    }
    
    return 'Outros';
}

// Renderização
function renderDashboard() {
    if (transactionsData.length === 0) {
        document.getElementById('emptyState').style.display = 'block';
        document.querySelector('.table-container').style.display = 'none';
    } else {
        document.getElementById('emptyState').style.display = 'none';
        document.querySelector('.table-container').style.display = 'block';
    }
    
    renderMetrics();
    renderCharts();
    renderTransactionsTable();
    setupFilters();
}

function renderMetrics() {
    const income = transactionsData
        .filter(t => t.amount > 0)
        .reduce((sum, t) => sum + t.amount, 0);
    
    const expenses = Math.abs(transactionsData
        .filter(t => t.amount < 0)
        .reduce((sum, t) => sum + t.amount, 0));
    
    const balance = income - expenses;
    
    document.getElementById('totalIncome').textContent = formatCurrency(income);
    document.getElementById('totalExpenses').textContent = formatCurrency(expenses);
    document.getElementById('netBalance').textContent = formatCurrency(balance);
    document.getElementById('totalTransactions').textContent = transactionsData.length;
}

function renderCharts() {
    renderCategoryChart();
    renderMonthlyChart();
}

function renderCategoryChart() {
    const expenses = transactionsData.filter(t => t.amount < 0);
    const categoryTotals = {};
    
    expenses.forEach(t => {
        if (!categoryTotals[t.category]) {
            categoryTotals[t.category] = 0;
        }
        categoryTotals[t.category] += Math.abs(t.amount);
    });
    
    const sortedCategories = Object.entries(categoryTotals)
        .sort((a, b) => b[1] - a[1])
        .slice(0, 10);
    
    const ctx = document.getElementById('categoryChart');
    
    if (charts.category) {
        charts.category.destroy();
    }
    
    if (sortedCategories.length === 0) {
        ctx.parentElement.innerHTML = '<h3>📊 Despesas por Categoria</h3><p style="text-align: center; color: var(--text-secondary);">Nenhuma despesa cadastrada</p>';
        return;
    }
    
    charts.category = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: sortedCategories.map(c => c[0]),
            datasets: [{
                data: sortedCategories.map(c => c[1]),
                backgroundColor: [
                    '#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF',
                    '#FF9F40', '#FF6384', '#C9CBCF', '#4BC0C0', '#FF6384'
                ]
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: {
                        boxWidth: 12,
                        font: {
                            size: 11
                        }
                    }
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            const label = context.label || '';
                            const value = formatCurrency(context.parsed);
                            const total = context.dataset.data.reduce((a, b) => a + b, 0);
                            const percentage = ((context.parsed / total) * 100).toFixed(1);
                            return `${label}: ${value} (${percentage}%)`;
                        }
                    }
                }
            }
        }
    });
}

function renderMonthlyChart() {
    const monthlyData = {};
    
    transactionsData.forEach(t => {
        const monthKey = t.date.toISOString().substring(0, 7);
        if (!monthlyData[monthKey]) {
            monthlyData[monthKey] = { income: 0, expenses: 0 };
        }
        
        if (t.amount > 0) {
            monthlyData[monthKey].income += t.amount;
        } else {
            monthlyData[monthKey].expenses += Math.abs(t.amount);
        }
    });
    
    const sortedMonths = Object.keys(monthlyData).sort();
    
    const ctx = document.getElementById('monthlyChart');
    
    if (charts.monthly) {
        charts.monthly.destroy();
    }
    
    if (sortedMonths.length === 0) {
        ctx.parentElement.innerHTML = '<h3>📈 Tendência Mensal</h3><p style="text-align: center; color: var(--text-secondary);">Nenhuma transação cadastrada</p>';
        return;
    }
    
    charts.monthly = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: sortedMonths.map(m => {
                const [year, month] = m.split('-');
                return `${month}/${year}`;
            }),
            datasets: [
                {
                    label: 'Receitas',
                    data: sortedMonths.map(m => monthlyData[m].income),
                    backgroundColor: '#10b981'
                },
                {
                    label: 'Despesas',
                    data: sortedMonths.map(m => monthlyData[m].expenses),
                    backgroundColor: '#ef4444'
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        callback: value => formatCurrency(value),
                        font: {
                            size: 10
                        }
                    }
                },
                x: {
                    ticks: {
                        font: {
                            size: 10
                        }
                    }
                }
            },
            plugins: {
                legend: {
                    labels: {
                        font: {
                            size: 11
                        }
                    }
                },
                tooltip: {
                    callbacks: {
                        label: context => {
                            return `${context.dataset.label}: ${formatCurrency(context.parsed.y)}`;
                        }
                    }
                }
            }
        }
    });
}

function renderTransactionsTable(filteredData = null) {
    const data = filteredData || transactionsData;
    const tbody = document.getElementById('transactionsBody');
    tbody.innerHTML = '';
    
    if (data.length === 0) {
        tbody.innerHTML = '<tr><td colspan="5" style="text-align: center; padding: 2rem; color: var(--text-secondary);">Nenhuma transação encontrada</td></tr>';
        return;
    }
    
    data.forEach(t => {
        const row = tbody.insertRow();
        row.innerHTML = `
            <td>${t.date.toLocaleDateString('pt-BR')}</td>
            <td>${t.description}</td>
            <td><span class="category-badge">${t.category}</span></td>
            <td class="${t.amount >= 0 ? 'amount-positive' : 'amount-negative'}">
                ${formatCurrency(t.amount)}
            </td>
            <td>
                <div class="action-buttons">
                    <button class="btn-sm btn-edit" onclick="openEditModal('${t.id}')">✏️</button>
                    <button class="btn-sm btn-delete" onclick="deleteTransaction('${t.id}')">🗑️</button>
                </div>
            </td>
        `;
    });
}

function setupFilters() {
    const categories = [...new Set(transactionsData.map(t => t.category))].sort();
    const categoryFilter = document.getElementById('categoryFilter');
    categoryFilter.innerHTML = '<option value="">Todas</option>';
    categories.forEach(cat => {
        const option = document.createElement('option');
        option.value = cat;
        option.textContent = cat;
        categoryFilter.appendChild(option);
    });
}

function applyFilters() {
    const categoryFilter = document.getElementById('categoryFilter').value;
    const typeFilter = document.getElementById('typeFilter').value;
    const searchFilter = document.getElementById('searchFilter').value.toLowerCase();
    
    let filtered = transactionsData;
    
    if (categoryFilter) {
        filtered = filtered.filter(t => t.category === categoryFilter);
    }
    
    if (typeFilter === 'income') {
        filtered = filtered.filter(t => t.amount > 0);
    } else if (typeFilter === 'expense') {
        filtered = filtered.filter(t => t.amount < 0);
    }
    
    if (searchFilter) {
        filtered = filtered.filter(t => 
            t.description.toLowerCase().includes(searchFilter)
        );
    }
    
    renderTransactionsTable(filtered);
}

function exportToCSV() {
    if (transactionsData.length === 0) {
        showMessage('Nenhuma transação para exportar', 'error');
        return;
    }
    
    const headers = ['Data', 'Descrição', 'Categoria', 'Valor'];
    const rows = transactionsData.map(t => [
        t.date.toLocaleDateString('pt-BR'),
        t.description,
        t.category,
        t.amount.toFixed(2)
    ]);
    
    let csv = headers.join(',') + '\n';
    rows.forEach(row => {
        csv += row.map(cell => `"${cell}"`).join(',') + '\n';
    });
    
    const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = 'financas_' + new Date().toISOString().split('T')[0] + '.csv';
    link.click();
    
    showMessage('Arquivo CSV exportado com sucesso!', 'success');
}

function showMessage(message, type) {
    const messageSection = document.getElementById('messageSection');
    messageSection.innerHTML = `<div class="${type}-message">${message}</div>`;
    
    setTimeout(() => {
        messageSection.innerHTML = '';
    }, 5000);
}

function formatCurrency(value) {
    return new Intl.NumberFormat('pt-BR', {
        style: 'currency',
        currency: 'BRL'
    }).format(value);
}
</script>
