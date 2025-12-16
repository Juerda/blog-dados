# 🚀 Guia Rápido - API Financeiro

## Iniciar API Localmente

### Passo 1: Instalar Dependências
```bash
cd api-financeiro
pip install -r requirements.txt
```

### Passo 2: Iniciar Servidor
```bash
python app.py
```

A API estará em **http://localhost:5000**

### Passo 3: Testar API
Abra outro terminal:
```bash
curl http://localhost:5000/api/health
```

## 📊 Acessar Banco de Dados

O arquivo `financeiro.db` será criado automaticamente na pasta `api-financeiro`.

Para visualizar os dados:
```bash
pip install sqlite-web
sqlite_web financeiro.db
```

Ou use [DB Browser for SQLite](https://sqlitebrowser.org/)

## 🔑 Endpoints Principais

- `POST /api/register` - Criar conta
- `POST /api/login` - Fazer login
- `GET /api/transactions` - Listar transações
- `POST /api/transactions` - Criar transação
- `POST /api/transactions/bulk` - Importar OFX
- `GET /api/admin/users` - Lista usuários (admin)
- `GET /api/admin/stats` - Estatísticas (admin)

## 📝 Nota Importante

**Para usar no dashboard web**, você precisa:

1. Manter a API rodando (`python app.py`)
2. O dashboard vai conectar em `http://localhost:5000`
3. Ou fazer deploy da API e atualizar `API_URL` no dashboard

## 🌐 Deploy (Vercel/Render)

Veja instruções completas no [README.md](README.md)
