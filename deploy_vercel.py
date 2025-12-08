#!/usr/bin/env python3
"""
Deploy para Vercel usando API
"""
import os
import json
import requests
import subprocess
from pathlib import Path

# Token do Vercel
VERCEL_TOKEN = "A2O3YmUIOk1fZrhiWNjm2h4K"
VERCEL_API = "https://api.vercel.com"

def get_project_id():
    """Obter ou criar projeto no Vercel"""
    headers = {
        "Authorization": f"Bearer {VERCEL_TOKEN}",
        "Content-Type": "application/json"
    }
    
    # Listar projetos
    response = requests.get(f"{VERCEL_API}/v9/projects", headers=headers)
    
    if response.status_code == 200:
        projects = response.json().get("projects", [])
        for project in projects:
            if project["name"] == "blog-dados":
                return project["id"]
    
    # Se não existe, criar novo
    print("📁 Criando novo projeto no Vercel...")
    create_response = requests.post(
        f"{VERCEL_API}/v10/projects",
        headers=headers,
        json={
            "name": "blog-dados",
            "framework": "other",
            "gitRepository": {
                "type": "github",
                "repo": "Juerda/blog-dados"
            }
        }
    )
    
    if create_response.status_code == 201:
        return create_response.json()["id"]
    else:
        print(f"❌ Erro ao criar projeto: {create_response.text}")
        return None

def trigger_deployment():
    """Disparar novo deployment via webhook"""
    headers = {
        "Authorization": f"Bearer {VERCEL_TOKEN}",
        "Content-Type": "application/json"
    }
    
    print("🚀 Iniciando deployment via GitHub integration...")
    
    # Usar a integração automática do Vercel com GitHub
    # O Vercel detectará automaticamente mudanças no repo
    
    response = requests.post(
        f"{VERCEL_API}/v12/integrations/deploy-hooks",
        headers=headers,
        json={
            "name": "blog-dados-webhook",
            "projectId": "prj_YuxiT4xJeR6iZRlcDCmsfKvpbtxe",
            "events": ["push"]
        }
    )
    
    if response.status_code in [200, 201, 409]:
        print(f"✅ Webhook de deployment criado!")
        print(f"\n🎉 Seu projeto está conectado ao Vercel!")
        print(f"📍 Acesse: https://vercel.com/dashboard")
        print(f"\n⏳ O deployment será automático quando você fizer push para main")
        return True
    else:
        print(f"❌ Erro ao criar webhook: {response.status_code}")
        print(f"   {response.text}")
        return False

if __name__ == "__main__":
    print("🔧 Deploy Vercel - Blog de Dados")
    print("=" * 50)
    
    if trigger_deployment():
        print("\n✨ Deploy iniciado!")
        print("Verifique https://vercel.com/dashboard para acompanhar")
    else:
        print("\n❌ Falha no deployment")
