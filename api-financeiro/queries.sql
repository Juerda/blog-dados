-- Queries úteis para administração do banco

-- ====================================
-- CONSULTAS DE USUÁRIOS
-- ====================================

-- Ver todos os usuários
SELECT 
    id,
    name,
    email,
    created_at,
    last_login,
    (SELECT COUNT(*) FROM transactions WHERE user_id = users.id) as total_transactions
FROM users
ORDER BY created_at DESC;

-- Usuários mais ativos
SELECT 
    u.name,
    u.email,
    COUNT(t.id) as total_transactions,
    SUM(CASE WHEN t.amount < 0 THEN ABS(t.amount) ELSE 0 END) as total_spent,
    SUM(CASE WHEN t.amount > 0 THEN t.amount ELSE 0 END) as total_income
FROM users u
LEFT JOIN transactions t ON t.user_id = u.id
GROUP BY u.id, u.name, u.email
ORDER BY total_transactions DESC;

-- Novos usuários (últimos 7 dias)
SELECT 
    name,
    email,
    created_at
FROM users
WHERE created_at >= NOW() - INTERVAL '7 days'
ORDER BY created_at DESC;

-- ====================================
-- CONSULTAS DE TRANSAÇÕES
-- ====================================

-- Todas as transações de um usuário
SELECT 
    date,
    description,
    category,
    amount,
    transaction_type,
    created_at
FROM transactions
WHERE user_id = 1
ORDER BY date DESC;

-- Transações por categoria
SELECT 
    category,
    COUNT(*) as total_transactions,
    SUM(ABS(amount)) as total_amount
FROM transactions
WHERE user_id = 1 AND amount < 0
GROUP BY category
ORDER BY total_amount DESC;

-- Maiores despesas
SELECT 
    date,
    description,
    category,
    ABS(amount) as amount
FROM transactions
WHERE user_id = 1 AND amount < 0
ORDER BY amount DESC
LIMIT 10;

-- Resumo mensal
SELECT 
    TO_CHAR(date, 'YYYY-MM') as month,
    SUM(CASE WHEN amount > 0 THEN amount ELSE 0 END) as income,
    SUM(CASE WHEN amount < 0 THEN ABS(amount) ELSE 0 END) as expenses,
    SUM(amount) as balance
FROM transactions
WHERE user_id = 1
GROUP BY TO_CHAR(date, 'YYYY-MM')
ORDER BY month DESC;

-- ====================================
-- ESTATÍSTICAS GERAIS
-- ====================================

-- Overview geral do sistema
SELECT 
    (SELECT COUNT(*) FROM users) as total_users,
    (SELECT COUNT(*) FROM transactions) as total_transactions,
    (SELECT SUM(CASE WHEN amount > 0 THEN amount ELSE 0 END) FROM transactions) as total_income,
    (SELECT SUM(CASE WHEN amount < 0 THEN ABS(amount) ELSE 0 END) FROM transactions) as total_expenses;

-- Categorias mais usadas
SELECT 
    category,
    COUNT(*) as usage_count,
    COUNT(DISTINCT user_id) as users_count
FROM transactions
GROUP BY category
ORDER BY usage_count DESC;

-- Transações por dia da semana
SELECT 
    TO_CHAR(date, 'Day') as day_of_week,
    COUNT(*) as total_transactions,
    AVG(ABS(amount)) as avg_amount
FROM transactions
WHERE amount < 0
GROUP BY TO_CHAR(date, 'Day'), EXTRACT(DOW FROM date)
ORDER BY EXTRACT(DOW FROM date);

-- ====================================
-- MANUTENÇÃO
-- ====================================

-- Limpar transações antigas (cuidado!)
-- DELETE FROM transactions WHERE date < '2024-01-01';

-- Backup de um usuário específico
SELECT * FROM transactions WHERE user_id = 1;

-- Encontrar duplicatas (mesmo FITID)
SELECT 
    external_id,
    user_id,
    COUNT(*) as count
FROM transactions
WHERE external_id IS NOT NULL
GROUP BY external_id, user_id
HAVING COUNT(*) > 1;

-- Remover duplicatas (manter a mais antiga)
DELETE FROM transactions
WHERE id NOT IN (
    SELECT MIN(id)
    FROM transactions
    WHERE external_id IS NOT NULL
    GROUP BY external_id, user_id
);

-- ====================================
-- ÍNDICES PARA PERFORMANCE
-- ====================================

-- Criar índices adicionais se necessário
-- CREATE INDEX idx_transactions_date ON transactions(date);
-- CREATE INDEX idx_transactions_category ON transactions(category);
-- CREATE INDEX idx_users_email ON users(email);
-- CREATE INDEX idx_transactions_user_date ON transactions(user_id, date DESC);
