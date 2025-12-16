-- Schema do banco de dados PostgreSQL
-- Execute estes comandos no Vercel Storage → Query para criar as tabelas manualmente

-- ====================================
-- Criar tabela de usuários
-- ====================================

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP
);

-- Índice para busca rápida por email
CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);

-- ====================================
-- Criar tabela de transações
-- ====================================

CREATE TABLE IF NOT EXISTS transactions (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    external_id VARCHAR(100),
    date DATE NOT NULL,
    description VARCHAR(255) NOT NULL,
    category VARCHAR(50) NOT NULL,
    amount NUMERIC(12, 2) NOT NULL,
    transaction_type VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índices para performance
CREATE INDEX IF NOT EXISTS idx_transactions_user_id ON transactions(user_id);
CREATE INDEX IF NOT EXISTS idx_transactions_date ON transactions(date);
CREATE INDEX IF NOT EXISTS idx_transactions_category ON transactions(category);
CREATE INDEX IF NOT EXISTS idx_transactions_external_id ON transactions(external_id);
CREATE INDEX IF NOT EXISTS idx_transactions_user_date ON transactions(user_id, date DESC);

-- ====================================
-- Trigger para atualizar updated_at
-- ====================================

-- Para tabela users
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER update_users_updated_at BEFORE UPDATE ON users
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

-- Para tabela transactions
CREATE TRIGGER update_transactions_updated_at BEFORE UPDATE ON transactions
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

-- ====================================
-- Inserir dados de teste (opcional)
-- ====================================

-- Usuário de teste (senha: 123456)
-- Hash gerado com: generate_password_hash('123456')
INSERT INTO users (name, email, password_hash) 
VALUES (
    'Usuário Teste',
    'teste@exemplo.com',
    'scrypt:32768:8:1$TESTEHASH12345'
) ON CONFLICT (email) DO NOTHING;

-- Transações de teste
INSERT INTO transactions (user_id, date, description, category, amount, transaction_type)
SELECT 
    u.id,
    CURRENT_DATE - INTERVAL '1 day' * generate_series(1, 10),
    'Transação Teste ' || generate_series(1, 10),
    CASE (generate_series(1, 10) % 3)
        WHEN 0 THEN 'Alimentação'
        WHEN 1 THEN 'Transporte'
        ELSE 'Lazer'
    END,
    -50.00 * generate_series(1, 10),
    'DEBIT'
FROM users u
WHERE u.email = 'teste@exemplo.com'
LIMIT 1;

-- ====================================
-- Verificar criação das tabelas
-- ====================================

-- Listar todas as tabelas
SELECT table_name 
FROM information_schema.tables 
WHERE table_schema = 'public'
ORDER BY table_name;

-- Ver estrutura da tabela users
SELECT 
    column_name,
    data_type,
    character_maximum_length,
    is_nullable,
    column_default
FROM information_schema.columns
WHERE table_name = 'users'
ORDER BY ordinal_position;

-- Ver estrutura da tabela transactions
SELECT 
    column_name,
    data_type,
    is_nullable,
    column_default
FROM information_schema.columns
WHERE table_name = 'transactions'
ORDER BY ordinal_position;

-- Listar índices
SELECT
    indexname,
    indexdef
FROM pg_indexes
WHERE schemaname = 'public'
ORDER BY tablename, indexname;

-- ====================================
-- Verificar dados
-- ====================================

-- Contar usuários
SELECT COUNT(*) as total_users FROM users;

-- Contar transações
SELECT COUNT(*) as total_transactions FROM transactions;

-- Ver últimos usuários cadastrados
SELECT id, name, email, created_at 
FROM users 
ORDER BY created_at DESC 
LIMIT 5;

-- Ver últimas transações
SELECT 
    t.id,
    u.name as user_name,
    t.date,
    t.description,
    t.amount
FROM transactions t
JOIN users u ON u.id = t.user_id
ORDER BY t.created_at DESC
LIMIT 10;

-- ====================================
-- Limpeza (cuidado!)
-- ====================================

-- Remover dados de teste
-- DELETE FROM transactions WHERE user_id IN (SELECT id FROM users WHERE email = 'teste@exemplo.com');
-- DELETE FROM users WHERE email = 'teste@exemplo.com';

-- Resetar sequências
-- ALTER SEQUENCE users_id_seq RESTART WITH 1;
-- ALTER SEQUENCE transactions_id_seq RESTART WITH 1;

-- Apagar tudo (MUITO CUIDADO!)
-- DROP TABLE IF EXISTS transactions CASCADE;
-- DROP TABLE IF EXISTS users CASCADE;
