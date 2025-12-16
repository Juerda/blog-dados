#!/bin/bash
# Script de deploy para Vercel

echo "🚀 Deploy da API Financeiro"
echo "============================"
echo ""

# Verificar se está na pasta correta
if [ ! -f "app.py" ]; then
    echo "❌ Erro: Execute este script na pasta api-financeiro"
    exit 1
fi

# Verificar se Vercel CLI está instalado
if ! command -v vercel &> /dev/null; then
    echo "📦 Instalando Vercel CLI..."
    npm i -g vercel
fi

echo "✅ Vercel CLI encontrado"
echo ""

# Fazer deploy
echo "🚀 Fazendo deploy..."
vercel --prod

echo ""
echo "✅ Deploy concluído!"
echo ""
echo "📝 Próximos passos:"
echo "1. Configure o banco de dados PostgreSQL no dashboard da Vercel"
echo "2. Adicione a variável SECRET_KEY"
echo "3. Renomeie POSTGRES_URL para DATABASE_URL"
echo "4. Atualize a URL da API no dashboard"
echo ""
echo "📖 Veja instruções completas em DEPLOY.md"
