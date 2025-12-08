#!/usr/bin/env python3
"""
Deploy automático para Vercel
Usa a integração GitHub automática do Vercel
"""

import subprocess
import json

print("🚀 DEPLOY VERCEL - Blog de Dados")
print("=" * 50)
print()

# Verificar se git está configurado
result = subprocess.run(['git', 'log', '--oneline', '-1'], capture_output=True, text=True)
if result.returncode == 0:
    print("✅ Git repository pronto")
    print(f"   Último commit: {result.stdout.strip()}")
else:
    print("❌ Erro com git")
    exit(1)

print()
print("🔗 Repositório: https://github.com/Juerda/blog-dados")
print("📍 Branch: main")
print()

# Instruções para o usuário
print("Para fazer o deploy, você pode usar 2 métodos:")
print()
print("OPÇÃO 1 (Recomendado - Automático):")
print("-" * 50)
print("1. Acesse: https://vercel.com/new")
print("2. Cole a URL: https://github.com/Juerda/blog-dados")
print("3. Clique em 'Deploy'")
print("4. Aguarde 2-3 minutos")
print()
print("OPÇÃO 2 (Via Vercel CLI):")
print("-" * 50)
print("1. Execute: npx vercel --prod")
print("2. Escolha 'Sim' para as perguntas")
print("3. Deploy vai acontecer em 2-3 minutos")
print()
print("=" * 50)
print()

# Criar um webhook simples
print("💡 Seu blog será atualizado automaticamente")
print("   quando você fazer push para a branch 'main'")
print()
print("✨ Blog estará disponível em:")
print("   https://blog-dados.vercel.app")
print()

# Informações finais
config = {
    "repository": "https://github.com/Juerda/blog-dados",
    "buildCommand": "pip install Pelican Markdown && pelican content -o output -s pelicanconf.py",
    "outputDirectory": "output",
    "framework": "other"
}

print("📋 Configuração do deploy:")
print(json.dumps(config, indent=2, ensure_ascii=False))
