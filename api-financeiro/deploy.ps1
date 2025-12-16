# Deploy da API Financeiro - Windows
# Execute: .\deploy.ps1

Write-Host "🚀 Deploy da API Financeiro" -ForegroundColor Cyan
Write-Host "============================" -ForegroundColor Cyan
Write-Host ""

# Verificar se está na pasta correta
if (-not (Test-Path "app.py")) {
    Write-Host "❌ Erro: Execute este script na pasta api-financeiro" -ForegroundColor Red
    exit 1
}

# Verificar se Vercel CLI está instalado
$vercelInstalled = Get-Command vercel -ErrorAction SilentlyContinue
if (-not $vercelInstalled) {
    Write-Host "📦 Instalando Vercel CLI..." -ForegroundColor Yellow
    npm i -g vercel
}

Write-Host "✅ Vercel CLI encontrado" -ForegroundColor Green
Write-Host ""

# Fazer deploy
Write-Host "🚀 Fazendo deploy..." -ForegroundColor Cyan
vercel --prod

Write-Host ""
Write-Host "✅ Deploy concluído!" -ForegroundColor Green
Write-Host ""
Write-Host "📝 Próximos passos:" -ForegroundColor Yellow
Write-Host "1. Configure o banco de dados PostgreSQL no dashboard da Vercel"
Write-Host "2. Adicione a variável SECRET_KEY"
Write-Host "3. Renomeie POSTGRES_URL para DATABASE_URL"
Write-Host "4. Atualize a URL da API no dashboard"
Write-Host ""
Write-Host "📖 Veja instruções completas em DEPLOY.md" -ForegroundColor Cyan
