#!/bin/bash

# Script de build para Vercel
# Instala dependências e gera site estático com Pelican

echo "📦 Instalando dependências..."
pip install --no-cache-dir Pelican Markdown

echo "🔨 Gerando site com Pelican..."
pelican content -o output -s pelicanconf.py

echo "✅ Build completo!"
echo "📁 Arquivos em: output/"
