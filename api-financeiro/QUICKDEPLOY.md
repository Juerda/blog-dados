# ⚡ Deploy Rápido - 5 Minutos

## 🎯 Objetivo
Colocar a API no ar com banco de dados PostgreSQL na Vercel.

## 📋 Checklist

### ✅ 1. Instalar Vercel CLI (1 min)
```bash
npm i -g vercel
```

### ✅ 2. Fazer Login (30 seg)
```bash
vercel login
```

### ✅ 3. Deploy Inicial (1 min)
```bash
cd api-financeiro
vercel --prod
```

Responda:
- ✅ Yes (deploy)
- ✅ Escolha sua conta
- ✅ No (não linkar projeto existente)
- ✅ api-financeiro (nome do projeto)
- ✅ ./ (diretório)
- ✅ No (não sobrescrever configs)

### ✅ 4. Criar Banco PostgreSQL (2 min)

1. Acesse: https://vercel.com/dashboard
2. **Storage** → **Create Database** → **Postgres**
3. Nome: `financeiro-db`
4. Região: São Paulo
5. **Create**

### ✅ 5. Conectar ao Projeto (1 min)

1. No database, clique **Connect Project**
2. Selecione `api-financeiro`
3. Marque todas as variáveis ✅
4. **Connect**

### ✅ 6. Configurar Variáveis (30 seg)

No projeto → **Settings** → **Environment Variables**:

1. Adicionar `SECRET_KEY`:
   - Value: `minha-chave-secreta-123456`
   
2. Renomear `POSTGRES_URL` para `DATABASE_URL`:
   - Editar → Mudar nome → Save

### ✅ 7. Redeploy (30 seg)
```bash
vercel --prod
```

### ✅ 8. Testar (10 seg)
```bash
curl https://SEU-PROJETO.vercel.app/api/health
```

Deve retornar:
```json
{"status":"ok","message":"API Financeiro funcionando"}
```

### ✅ 9. Atualizar Dashboard (1 min)

No arquivo `content/pages/dashboard.md`, linha ~813:

```javascript
const API_URL = 'https://SEU-PROJETO.vercel.app/api';
```

Fazer commit e push:
```bash
git add .
git commit -m "Atualiza URL da API"
git push
```

## 🎉 PRONTO!

Sua API está no ar com:
- ✅ PostgreSQL configurado
- ✅ Tabelas criadas automaticamente
- ✅ HTTPS gratuito
- ✅ Deploy automático

## 📱 URLs Importantes

- **API:** https://SEU-PROJETO.vercel.app
- **Dashboard:** https://blog-dados.vercel.app/dashboard
- **Admin DB:** https://vercel.com/dashboard/stores

## 🆘 Problemas?

### Erro 500 na API
```bash
vercel logs
```

### Tabelas não criadas
Faça uma requisição POST para criar:
```bash
curl -X POST https://SEU-PROJETO.vercel.app/api/register \
  -H "Content-Type: application/json" \
  -d '{"name":"Test","email":"test@test.com","password":"123456"}'
```

### Dashboard não conecta
Verifique CORS e URL da API no código.

## 🚀 Comando Único (Windows)
```powershell
.\deploy.ps1
```

## 🚀 Comando Único (Linux/Mac)
```bash
./deploy.sh
```

---

**Tempo total:** ~7 minutos  
**Custo:** R$ 0,00 (Vercel Free Tier)  
**Uptime:** 99.99%
