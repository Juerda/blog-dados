@echo off
REM Script para gerenciar o blog Pelican no Windows

if "%1"=="build" (
    echo Compilando o site...
    pelican content -o output -s pelicanconf.py
    echo Compilacao concluida!
    
) else if "%1"=="serve" (
    echo Iniciando servidor local em http://localhost:8000
    cd output
    python -m http.server 8000
    cd ..
    
) else if "%1"=="dev" (
    echo Modo desenvolvimento com recarregamento automatico...
    pelican -l -r content -o output -s pelicanconf.py
    
) else if "%1"=="clean" (
    echo Limpando arquivos gerados...
    rmdir /s /q output
    echo Limpeza concluida!
    
) else if "%1"=="install" (
    echo Instalando dependencias...
    pip install -r requirements.txt
    echo Dependencias instaladas!
    
) else (
    echo Comandos disponiveis:
    echo.
    echo   blog.bat build  - Compila o site
    echo   blog.bat serve  - Inicia servidor local
    echo   blog.bat dev    - Modo desenvolvimento com recarregamento
    echo   blog.bat clean  - Remove arquivos gerados
    echo   blog.bat install - Instala dependencias
    echo.
)
