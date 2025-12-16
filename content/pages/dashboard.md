Title: Dashboard Financeiro
Date: 2025-12-16
Slug: dashboard
Summary: Análise inteligente de extratos bancários OFX

<div id="financial-dashboard">
    <style>
        .dashboard-container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 2rem;
        }
        
        .dashboard-header {
            text-align: center;
            margin-bottom: 3rem;
        }
        
        .dashboard-header h1 {
            font-size: 2.5rem;
            color: var(--primary-blue);
            margin-bottom: 0.5rem;
        }
        
        .dashboard-header p {
            font-size: 1.1rem;
            color: var(--text-secondary);
        }
        
        .upload-section {
            background: var(--bg-secondary);
            border-radius: 12px;
            padding: 2rem;
            margin-bottom: 2rem;
            text-align: center;
            border: 2px dashed var(--border-color);
        }
        
        .upload-section.dragover {
            border-color: var(--primary-blue);
            background: rgba(0, 102, 204, 0.05);
        }
        
        .file-input-wrapper {
            position: relative;
            display: inline-block;
        }
        
        .file-input-wrapper input[type="file"] {
            display: none;
        }
        
        .file-input-label {
            display: inline-block;
            padding: 1rem 2rem;
            background: var(--primary-blue);
            color: white;
            border-radius: 8px;
            cursor: pointer;
            font-weight: 600;
            transition: all 0.3s;
        }
        
        .file-input-label:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0, 102, 204, 0.3);
        }
        
        .metrics-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1.5rem;
            margin-bottom: 2rem;
        }
        
        .metric-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 1.5rem;
            border-radius: 12px;
            color: white;
            text-align: center;
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
            font-size: 2rem;
            font-weight: bold;
        }
        
        .charts-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(500px, 1fr));
            gap: 2rem;
            margin-bottom: 2rem;
        }
        
        .chart-card {
            background: var(--bg-secondary);
            padding: 1.5rem;
            border-radius: 12px;
            border: 1px solid var(--border-color);
        }
        
        .chart-card h3 {
            margin-top: 0;
            margin-bottom: 1rem;
            color: var(--text-primary);
        }
        
        .transactions-section {
            background: var(--bg-secondary);
            padding: 1.5rem;
            border-radius: 12px;
            border: 1px solid var(--border-color);
        }
        
        .filters {
            display: flex;
            gap: 1rem;
            margin-bottom: 1.5rem;
            flex-wrap: wrap;
        }
        
        .filter-group {
            flex: 1;
            min-width: 200px;
        }
        
        .filter-group label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: 600;
            color: var(--text-primary);
        }
        
        .filter-group select,
        .filter-group input {
            width: 100%;
            padding: 0.5rem;
            border: 1px solid var(--border-color);
            border-radius: 6px;
            background: var(--bg-primary);
            color: var(--text-primary);
        }
        
        .transactions-table {
            width: 100%;
            border-collapse: collapse;
            overflow-x: auto;
            display: block;
        }
        
        .transactions-table thead {
            background: var(--bg-primary);
            position: sticky;
            top: 0;
        }
        
        .transactions-table th,
        .transactions-table td {
            padding: 1rem;
            text-align: left;
            border-bottom: 1px solid var(--border-color);
        }
        
        .transactions-table th {
            font-weight: 600;
            color: var(--text-primary);
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
            font-size: 0.85rem;
            background: var(--primary-blue);
            color: white;
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
        
        .export-btn {
            padding: 0.75rem 1.5rem;
            background: var(--primary-blue);
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-weight: 600;
            margin-top: 1rem;
        }
        
        .export-btn:hover {
            opacity: 0.9;
        }
        
        @media (max-width: 768px) {
            .charts-grid {
                grid-template-columns: 1fr;
            }
            
            .transactions-table {
                font-size: 0.85rem;
            }
            
            .transactions-table th,
            .transactions-table td {
                padding: 0.5rem;
            }
        }
    </style>
    
    <div class="dashboard-container">
        <div class="dashboard-header">
            <h1>💰 Dashboard Financeiro</h1>
            <p>Análise inteligente de extratos bancários OFX</p>
        </div>
        
        <div class="upload-section" id="uploadSection">
            <h3>📁 Carregar Extrato Bancário</h3>
            <p>Arraste o arquivo OFX aqui ou clique para selecionar</p>
            <div class="file-input-wrapper">
                <input type="file" id="ofxFile" accept=".ofx,.OFX" />
                <label for="ofxFile" class="file-input-label">Escolher Arquivo OFX</label>
            </div>
            <p style="margin-top: 1rem; font-size: 0.9rem; color: var(--text-secondary);">
                Formato suportado: OFX (Open Financial Exchange)
            </p>
        </div>
        
        <div id="loadingSection" style="display: none;" class="loading">
            <div class="loading-spinner"></div>
            <p>Processando extrato bancário...</p>
        </div>
        
        <div id="errorSection" style="display: none;" class="error-message"></div>
        
        <div id="dashboardContent" style="display: none;">
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
            
            <div class="charts-grid">
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
                        <select id="categoryFilter">
                            <option value="">Todas</option>
                        </select>
                    </div>
                    <div class="filter-group">
                        <label>Tipo</label>
                        <select id="typeFilter">
                            <option value="">Todas</option>
                            <option value="income">Receitas</option>
                            <option value="expense">Despesas</option>
                        </select>
                    </div>
                    <div class="filter-group">
                        <label>Buscar</label>
                        <input type="text" id="searchFilter" placeholder="Buscar descrição..." />
                    </div>
                </div>
                
                <div style="overflow-x: auto;">
                    <table class="transactions-table">
                        <thead>
                            <tr>
                                <th>Data</th>
                                <th>Descrição</th>
                                <th>Categoria</th>
                                <th>Valor</th>
                            </tr>
                        </thead>
                        <tbody id="transactionsBody"></tbody>
                    </table>
                </div>
                
                <button class="export-btn" onclick="exportToCSV()">📥 Exportar CSV</button>
            </div>
        </div>
    </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>

<script>
// Variáveis globais
let transactionsData = [];
let charts = {
    category: null,
    monthly: null
};

// Categorias brasileiras
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

// Configurar upload
document.getElementById('ofxFile').addEventListener('change', handleFileSelect);

const uploadSection = document.getElementById('uploadSection');
uploadSection.addEventListener('dragover', (e) => {
    e.preventDefault();
    uploadSection.classList.add('dragover');
});

uploadSection.addEventListener('dragleave', () => {
    uploadSection.classList.remove('dragover');
});

uploadSection.addEventListener('drop', (e) => {
    e.preventDefault();
    uploadSection.classList.remove('dragover');
    const file = e.dataTransfer.files[0];
    if (file && file.name.toLowerCase().endsWith('.ofx')) {
        processOFXFile(file);
    }
});

function handleFileSelect(event) {
    const file = event.target.files[0];
    if (file) {
        processOFXFile(file);
    }
}

function showLoading() {
    document.getElementById('loadingSection').style.display = 'block';
    document.getElementById('dashboardContent').style.display = 'none';
    document.getElementById('errorSection').style.display = 'none';
}

function showError(message) {
    document.getElementById('errorSection').textContent = message;
    document.getElementById('errorSection').style.display = 'block';
    document.getElementById('loadingSection').style.display = 'none';
}

function showDashboard() {
    document.getElementById('dashboardContent').style.display = 'block';
    document.getElementById('loadingSection').style.display = 'none';
}

function processOFXFile(file) {
    showLoading();
    
    const reader = new FileReader();
    reader.onload = function(e) {
        try {
            const ofxData = e.target.result;
            const transactions = parseOFX(ofxData);
            
            if (transactions.length === 0) {
                showError('Nenhuma transação encontrada no arquivo OFX');
                return;
            }
            
            transactionsData = transactions;
            categorizeTransactions();
            renderDashboard();
            showDashboard();
        } catch (error) {
            showError('Erro ao processar arquivo OFX: ' + error.message);
        }
    };
    reader.readAsText(file);
}

function parseOFX(ofxText) {
    const transactions = [];
    
    try {
        // Parser simples de OFX usando regex
        const stmttrnPattern = /<STMTTRN>([\s\S]*?)<\/STMTTRN>/g;
        const matches = ofxText.matchAll(stmttrnPattern);
        
        for (const match of matches) {
            const trnBlock = match[1];
            
            // Extrair campos
            const dtposted = trnBlock.match(/<DTPOSTED>(\d+)/)?.[1];
            const trnamt = trnBlock.match(/<TRNAMT>([-\d.]+)/)?.[1];
            const fitid = trnBlock.match(/<FITID>([^<]+)/)?.[1];
            const memo = trnBlock.match(/<MEMO>([^<]*)/)?.[1] || '';
            const name = trnBlock.match(/<NAME>([^<]*)/)?.[1] || '';
            const trntype = trnBlock.match(/<TRNTYPE>([^<]+)/)?.[1];
            
            if (!dtposted || !trnamt) continue;
            
            // Parsear data (formato YYYYMMDD)
            const year = parseInt(dtposted.substring(0, 4));
            const month = parseInt(dtposted.substring(4, 6)) - 1;
            const day = parseInt(dtposted.substring(6, 8));
            
            // Descrição: priorizar MEMO, depois NAME
            let description = memo || name || 'Sem descrição';
            description = description.trim();
            
            // Limpar descrição (remover aspas extras)
            description = description.replace(/^["']|["']$/g, '');
            
            transactions.push({
                date: new Date(year, month, day),
                description: description,
                amount: parseFloat(trnamt),
                type: trntype || 'OTHER',
                id: fitid || Date.now().toString(),
                category: null
            });
        }
        
        if (transactions.length === 0) {
            throw new Error('Nenhuma transação encontrada no arquivo');
        }
        
        return transactions.sort((a, b) => b.date - a.date);
        
    } catch (error) {
        console.error('Erro ao processar OFX:', error);
        throw new Error('Erro ao processar arquivo OFX: ' + error.message);
    }
}

function categorizeTransactions() {
    transactionsData.forEach(transaction => {
        const desc = transaction.description.toLowerCase();
        
        // Receitas
        if (transaction.amount > 0) {
            transaction.category = 'Receitas';
            return;
        }
        
        // Buscar categoria por palavras-chave
        for (const [category, keywords] of Object.entries(CATEGORIES)) {
            for (const keyword of keywords) {
                if (desc.includes(keyword)) {
                    transaction.category = category;
                    return;
                }
            }
        }
        
        transaction.category = 'Outros';
    });
}

function renderDashboard() {
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
            plugins: {
                legend: {
                    position: 'right'
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
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        callback: value => formatCurrency(value)
                    }
                }
            },
            plugins: {
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
    
    data.forEach(t => {
        const row = tbody.insertRow();
        row.innerHTML = `
            <td>${t.date.toLocaleDateString('pt-BR')}</td>
            <td>${t.description}</td>
            <td><span class="category-badge">${t.category}</span></td>
            <td class="${t.amount >= 0 ? 'amount-positive' : 'amount-negative'}">
                ${formatCurrency(t.amount)}
            </td>
        `;
    });
}

function setupFilters() {
    // Popular filtro de categorias
    const categories = [...new Set(transactionsData.map(t => t.category))].sort();
    const categoryFilter = document.getElementById('categoryFilter');
    categoryFilter.innerHTML = '<option value="">Todas</option>';
    categories.forEach(cat => {
        const option = document.createElement('option');
        option.value = cat;
        option.textContent = cat;
        categoryFilter.appendChild(option);
    });
    
    // Event listeners para filtros
    document.getElementById('categoryFilter').addEventListener('change', applyFilters);
    document.getElementById('typeFilter').addEventListener('change', applyFilters);
    document.getElementById('searchFilter').addEventListener('input', applyFilters);
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
    link.download = 'transacoes_' + new Date().toISOString().split('T')[0] + '.csv';
    link.click();
}

function formatCurrency(value) {
    return new Intl.NumberFormat('pt-BR', {
        style: 'currency',
        currency: 'BRL'
    }).format(value);
}
</script>
