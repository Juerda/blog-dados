@echo off
REM Script para fazer push para GitHub automaticamente

if "%1"=="" (
    echo Digite uma mensagem de commit:
    echo.
    echo Uso: push.bat "Sua mensagem de commit aqui"
    echo.
    echo Exemplo: push.bat "Adicionado novo post sobre analise"
    echo.
    exit /b 1
)

echo.
echo ========================================
echo Git Push para GitHub
echo ========================================
echo.

REM Adicionar todos os arquivos
echo [1/3] Adicionando arquivos...
git add .

REM Fazer commit
echo [2/3] Fazendo commit...
git commit -m "%1"

REM Fazer push
echo [3/3] Fazendo push para GitHub...
git push

echo.
echo ========================================
echo Sucesso! Arquivos enviados para GitHub
echo ========================================
echo.
pause
