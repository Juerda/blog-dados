@echo off
REM Deploy para Vercel usando npx (sem npm global)

cd /d "c:\Users\jorda\OneDrive\Documentos\Projeto - Blog"

echo.
echo =====================================================
echo  DEPLOY VERCEL - Blog de Dados
echo =====================================================
echo.

REM Verificar se o node_modules existe
if not exist node_modules (
    echo Instalando dependencias...
    call npx --yes vercel@latest --token A2O3YmUIOk1fZrhiWNjm2h4K --prod --confirm
) else (
    echo Fazendo deploy...
    call npx vercel@latest --token A2O3YmUIOk1fZrhiWNjm2h4K --prod --confirm
)

echo.
echo Deployment completo!
echo Verifique: https://vercel.com/dashboard
echo.
pause
