#!/bin/bash

# Script para gerenciar o blog Pelican no macOS/Linux

case "$1" in
    build)
        echo "Compilando o site..."
        pelican content -o output -s pelicanconf.py
        echo "Compilação concluída!"
        ;;
    serve)
        echo "Iniciando servidor local em http://localhost:8000"
        cd output || exit
        python3 -m http.server 8000
        cd - || exit
        ;;
    dev)
        echo "Modo desenvolvimento com recarregamento automático..."
        pelican -l -r content -o output -s pelicanconf.py
        ;;
    clean)
        echo "Limpando arquivos gerados..."
        rm -rf output
        echo "Limpeza concluída!"
        ;;
    install)
        echo "Instalando dependências..."
        pip install -r requirements.txt
        echo "Dependências instaladas!"
        ;;
    *)
        echo "Comandos disponíveis:"
        echo ""
        echo "  ./blog.sh build   - Compila o site"
        echo "  ./blog.sh serve   - Inicia servidor local"
        echo "  ./blog.sh dev     - Modo desenvolvimento com recarregamento"
        echo "  ./blog.sh clean   - Remove arquivos gerados"
        echo "  ./blog.sh install - Instala dependências"
        echo ""
        ;;
esac
