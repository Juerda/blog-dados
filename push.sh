#!/bin/bash

# Script para fazer push para GitHub automaticamente

if [ -z "$1" ]; then
    echo ""
    echo "========================================"
    echo "Git Push para GitHub"
    echo "========================================"
    echo ""
    echo "Digite uma mensagem de commit:"
    echo ""
    echo "Uso: ./push.sh \"Sua mensagem de commit aqui\""
    echo ""
    echo "Exemplo: ./push.sh \"Adicionado novo post sobre analise\""
    echo ""
    exit 1
fi

echo ""
echo "========================================"
echo "Git Push para GitHub"
echo "========================================"
echo ""

# Adicionar todos os arquivos
echo "[1/3] Adicionando arquivos..."
git add .

# Fazer commit
echo "[2/3] Fazendo commit..."
git commit -m "$1"

# Fazer push
echo "[3/3] Fazendo push para GitHub..."
git push

echo ""
echo "========================================"
echo "Sucesso! Arquivos enviados para GitHub"
echo "========================================"
echo ""
