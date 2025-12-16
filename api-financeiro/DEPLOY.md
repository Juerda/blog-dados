# 🚀 Deploy da API Financeiro na Vercel

## Passo a Passo Completo

### 1️⃣ Instalar Vercel CLI

```bash
npm i -g vercel
```

### 2️⃣ Fazer Login na Vercel

```bash
vercel login
```

### 3️⃣ Criar Banco de Dados PostgreSQL na Vercel

1. Acesse [vercel.com/dashboard](https://vercel.com/dashboard)
2. Clique em **Storage** → **Create Database**
3. Escolha **Postgres**
4. Nome: `financeiro-db`
5. Região: Choose closest to you (ex: São Paulo)
6. Clique em **Create**

### 4️⃣ Deploy da API

```bash
cd api-financeiro
vercel --prod
```

Siga as perguntas:
- Set up and deploy? **Y**
- Which scope? (selecione sua conta)
- Link to existing project? **N**
- Project name? `api-financeiro` (ou outro nome)
- Directory? **./** (deixe em branco)
- Override settings? **N**

### 5️⃣ Conectar Banco de Dados

No dashboard da Vercel:

1. Vá em **Storage** → Seu database `financeiro-db`
2. Clique em **Connect Project**
3. Selecione o projeto `api-financeiro`
4. Marque as variáveis:
   - ✅ `POSTGRES_URL`
   - ✅ `POSTGRES_PRISMA_URL`
   - ✅ `POSTGRES_URL_NON_POOLING`
5. Clique em **Connect**

### 6️⃣ Adicionar SECRET_KEY

No projeto da Vercel:

1. Vá em **Settings** → **Environment Variables**
2. Adicione:
   - **Key:** `SECRET_KEY`
   - **Value:** `sua-chave-secreta-super-segura-aqui-123456`
   - **Environments:** Production, Preview, Development
3. Clique em **Save**

### 7️⃣ Renomear DATABASE_URL

1. Em **Environment Variables**, encontre `POSTGRES_URL`
2. Clique em **Edit**
3. Mude o nome para: `DATABASE_URL`
4. Salve

### 8️⃣ Fazer Redeploy

```bash
vercel --prod
```

### 9️⃣ Testar API

Sua API estará em: `https://api-financeiro-seu-usuario.vercel.app`

Teste:
```bash
curl https://api-financeiro-seu-usuario.vercel.app/api/health
```

Deve retornar:
```json
{"status": "ok", "message": "API Financeiro funcionando"}
```

### 🔟 Atualizar Dashboard

No arquivo `dashboard.md`, linha ~815:

```javascript
// Trocar de:
const API_URL = 'http://localhost:5000/api';

// Para:
const API_URL = 'https://api-financeiro-seu-usuario.vercel.app/api';
```

### ✅ Pronto!

Agora você tem:
- ✅ API rodando na Vercel
- ✅ PostgreSQL configurado
- ✅ Tabelas criadas automaticamente
- ✅ HTTPS gratuito
- ✅ Deploy automático no git push

## 📊 Acessar Banco de Dados

### Via Vercel Dashboard

1. Vá em **Storage** → `financeiro-db`
2. Clique em **Data** → **Browse Data**
3. Você verá as tabelas `users` e `transactions`

### Via pgAdmin ou DBeaver

1. Copie a string de conexão em **Settings** → `.env.local`
2. Use em qualquer cliente PostgreSQL

### Via SQL Editor (Vercel)

1. **Storage** → `financeiro-db` → **Query**
2. Execute queries SQL:

```sql
-- Ver todos os usuários
SELECT id, name, email, created_at, last_login FROM users;

-- Ver transações de um usuário
SELECT * FROM transactions WHERE user_id = 1 ORDER BY date DESC;

-- Estatísticas
SELECT 
    COUNT(DISTINCT user_id) as total_users,
    COUNT(*) as total_transactions,
    SUM(CASE WHEN amount > 0 THEN amount ELSE 0 END) as total_income,
    SUM(CASE WHEN amount < 0 THEN ABS(amount) ELSE 0 END) as total_expenses
FROM transactions;
```

## 🔄 Comandos Úteis

```bash
# Ver logs da API
vercel logs

# Ver deployments
vercel ls

# Remover deployment antigo
vercel rm nome-do-deploy

# Adicionar variável de ambiente
vercel env add SECRET_KEY

# Listar variáveis
vercel env ls
```

## 🐛 Troubleshooting

### Erro: "No module named 'psycopg2'"

Certifique-se que `psycopg2-binary==2.9.9` está em `requirements.txt`

### Erro: "relation 'users' does not exist"

As tabelas são criadas automaticamente no primeiro acesso. Tente:
```bash
curl -X POST https://sua-api.vercel.app/api/register \
  -H "Content-Type: application/json" \
  -d '{"name":"Test","email":"test@test.com","password":"123456"}'
```

### Erro CORS

Certifique-se que CORS está configurado:
```python
CORS(app, resources={r"/api/*": {"origins": ["*"]}})
```

## 📱 Próximos Passos

1. ✅ Deploy da API - **FEITO**
2. ✅ Banco PostgreSQL - **FEITO**
3. ⬜ Atualizar `API_URL` no dashboard
4. ⬜ Testar cadastro/login
5. ⬜ Importar OFX
6. ⬜ Adicionar mais funcionalidades

## 🎉 Resultado Final

Agora você tem uma API de produção com:
- ✅ Autenticação JWT
- ✅ Banco de dados PostgreSQL
- ✅ Tabelas `users` e `transactions`
- ✅ Deploy automático
- ✅ HTTPS gratuito
- ✅ Escalabilidade automática
- ✅ Backups automáticos
- ✅ 99.99% uptime
