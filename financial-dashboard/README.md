# 💰 Dashboard Financeiro Pessoal

> Análise inteligente de extratos bancários OFX com categorização automática usando LLM local

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.29+-red?logo=streamlit)](https://streamlit.io/)
[![Ollama](https://img.shields.io/badge/Ollama-LLM%20Local-green)](https://ollama.ai/)

---

## 🌟 Características Principais

- ✅ **Leitura de OFX** - Importa extratos bancários de qualquer banco brasileiro
- ✅ **Categorização Inteligente** - LLM local analisa e categoriza cada transação
- ✅ **Aprendizado de Padrões** - Sistema aprende com suas transações para categorizar mais rápido
- ✅ **Visualizações Interativas** - Gráficos de pizza, barras, tendências mensais
- ✅ **Análises Detalhadas** - Top despesas, receitas, resumos por categoria
- ✅ **Filtros Avançados** - Por categoria, tipo, período
- ✅ **Export CSV** - Exporte dados para análises externas
- ✅ **100% Local e Privado** - Seus dados não saem do seu computador

---

## 📋 Índice

1. [Pré-requisitos](#-pré-requisitos)
2. [Instalação](#-instalação)
3. [Como Usar](#-como-usar)
4. [Estrutura do Projeto](#-estrutura-do-projeto)
5. [Configuração do Ollama](#-configuração-do-ollama)
6. [Categorias Disponíveis](#-categorias-disponíveis)
7. [Comandos Úteis](#-comandos-úteis)
8. [Solução de Problemas](#-solução-de-problemas)

---

## 📋 Pré-requisitos

### Software Necessário

| Software | Versão | Download | Verificar |
|----------|--------|----------|-----------|
| **Python** | 3.8+ | [python.org](https://www.python.org/downloads/) | `python --version` |
| **Ollama** | Latest | [ollama.ai](https://ollama.ai/) | `ollama --version` |
| **pip** | Latest | (incluído com Python) | `pip --version` |

### Instalar Ollama

**Windows:**
```powershell
# Baixar instalador em https://ollama.ai/download/windows
# Executar o instalador
# Verificar instalação
ollama --version
```

**macOS:**
```bash
# Baixar instalador em https://ollama.ai/download/mac
# Ou via Homebrew
brew install ollama
```

**Linux:**
```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

### Baixar Modelo LLM

Após instalar Ollama, baixe um modelo:

```bash
# Modelo recomendado (leve e rápido)
ollama pull llama3.2

# Alternativas
ollama pull llama2      # Modelo maior, mais preciso
ollama pull mistral     # Bom equilíbrio
ollama pull phi         # Muito leve
```

---

## 🚀 Instalação

### Passo 1: Clone ou Baixe o Projeto

```bash
# Se estiver no repositório do blog
cd financial-dashboard

# Ou navegue até a pasta
cd c:\Users\jorda\OneDrive\Documentos\Projeto - Blog\financial-dashboard
```

### Passo 2: Crie Ambiente Virtual (Recomendado)

**Windows:**
```powershell
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Passo 3: Instale Dependências

```bash
pip install -r requirements.txt
```

**Dependências instaladas:**
- `streamlit` - Interface web
- `pandas` - Manipulação de dados
- `ofxparse` - Leitura de arquivos OFX
- `ollama` - Integração com LLM local
- `plotly` - Gráficos interativos

---

## 💻 Como Usar

### Passo 1: Iniciar Ollama (se não estiver rodando)

```bash
# Em um terminal separado
ollama serve
```

### Passo 2: Executar o Dashboard

```bash
streamlit run app.py
```

O dashboard abrirá automaticamente em: **http://localhost:8501**

### Passo 3: Fazer Upload do Extrato

1. **Obter extrato OFX do seu banco:**
   - Acesse o site ou app do banco
   - Vá em "Extratos" ou "Exportar"
   - Escolha formato **OFX** ou **Money** (são equivalentes)
   - Baixe o arquivo

2. **Fazer upload no dashboard:**
   - Na barra lateral, clique em "Browse files"
   - Selecione o arquivo `.ofx` baixado
   - Aguarde o processamento

### Passo 4: Categorizar Transações

1. Após o upload, clique em **"🤖 Categorizar com LLM"**
2. Aguarde enquanto o LLM analisa cada transação
3. O sistema aprenderá padrões automaticamente

### Passo 5: Explorar Análises

- **Visão Geral:** Gráficos de pizza, barras e tendências
- **Transações:** Lista completa com filtros
- **Análises:** Top despesas/receitas, resumos
- **Configurações:** Padrões aprendidos, exports

---

## 📂 Estrutura do Projeto

```
financial-dashboard/
│
├── 📄 app.py                      # Aplicação Streamlit principal
├── 📄 requirements.txt            # Dependências Python
├── 📄 README.md                   # Esta documentação
│
├── 📁 utils/                      # Utilitários
│   └── ofx_parser.py             # Parser de arquivos OFX
│
├── 📁 models/                     # Modelos de IA
│   └── categorizer.py            # Categorizador com LLM
│
└── 📁 data/                       # Dados persistidos
    └── learned_patterns.json     # Padrões aprendidos (gerado automaticamente)
```

### Descrição dos Arquivos

| Arquivo | Descrição |
|---------|-----------|
| `app.py` | Interface Streamlit com dashboard completo |
| `utils/ofx_parser.py` | Lê e processa arquivos OFX de bancos |
| `models/categorizer.py` | Categoriza transações usando Ollama (LLM local) |
| `data/learned_patterns.json` | Cache de padrões aprendidos para categorização rápida |

---

## 🤖 Configuração do Ollama

### Modelos Disponíveis

O dashboard suporta vários modelos Ollama:

| Modelo | Tamanho | RAM Necessária | Velocidade | Precisão |
|--------|---------|----------------|------------|----------|
| **llama3.2** ⭐ | 2GB | 4GB | Rápido | Alta |
| **mistral** | 4GB | 8GB | Médio | Muito Alta |
| **llama2** | 7GB | 16GB | Lento | Excelente |
| **phi** | 1.5GB | 3GB | Muito Rápido | Boa |

**Recomendação:** Use `llama3.2` para melhor equilíbrio.

### Instalar Modelo

```bash
# Modelo recomendado
ollama pull llama3.2

# Listar modelos instalados
ollama list

# Testar modelo
ollama run llama3.2
```

### Trocar Modelo no Dashboard

1. Na barra lateral, use o seletor "Modelo LLM"
2. Escolha o modelo desejado
3. Categorize novamente

---

## 🏷️ Categorias Disponíveis

O sistema categoriza automaticamente em:

| Categoria | Exemplos de Transações |
|-----------|------------------------|
| **Alimentação** | Supermercado, restaurante, iFood, padaria |
| **Transporte** | Uber, 99, gasolina, estacionamento, pedágio |
| **Moradia** | Aluguel, condomínio, IPTU, água, luz, internet |
| **Saúde** | Farmácia, médico, plano de saúde, dentista |
| **Educação** | Escola, faculdade, cursos, livros |
| **Lazer** | Cinema, Netflix, Spotify, academia, viagens |
| **Vestuário** | Roupas, calçados, shopping |
| **Serviços** | Cabeleireiro, barbeiro, lavanderia |
| **Investimentos** | Aplicações, poupança, CDB, ações |
| **Receitas** | Salário, freelance, vendas, reembolsos |
| **Transferências** | PIX, TED, DOC |
| **Outros** | Transações não categorizadas |

### Aprendizado de Padrões

O sistema aprende automaticamente:
- ✅ Após categorizar, salva padrões em `data/learned_patterns.json`
- ✅ Próximas transações similares são categorizadas instantaneamente
- ✅ Padrões podem ser limpos em **Configurações → Limpar Padrões**

---

## 🔧 Comandos Úteis

### Executar Dashboard

```bash
# Modo normal
streamlit run app.py

# Modo com porta customizada
streamlit run app.py --server.port 8502

# Modo sem auto-reload
streamlit run app.py --server.runOnSave false
```

### Gerenciar Ollama

```bash
# Iniciar servidor Ollama
ollama serve

# Listar modelos instalados
ollama list

# Baixar novo modelo
ollama pull llama3.2

# Remover modelo
ollama rm llama2

# Testar modelo interativamente
ollama run llama3.2
```

### Gerenciar Ambiente Python

```bash
# Ativar ambiente virtual
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# Instalar/atualizar dependências
pip install -r requirements.txt

# Listar pacotes instalados
pip list

# Desativar ambiente
deactivate
```

---

## 🐛 Solução de Problemas

### Ollama não está disponível

**Erro:** `Ollama não está rodando`

**Solução:**
```bash
# Abra um novo terminal e execute
ollama serve

# Deixe rodando em background
```

---

### Modelo não encontrado

**Erro:** `model 'llama3.2' not found`

**Solução:**
```bash
# Baixar modelo
ollama pull llama3.2

# Verificar se foi instalado
ollama list
```

---

### Erro ao processar OFX

**Erro:** `Erro ao processar arquivo OFX`

**Possíveis causas:**
1. Arquivo corrompido ou formato inválido
2. Banco usa formato OFX não padrão

**Solução:**
- Baixe novamente o extrato do banco
- Certifique-se de escolher formato **OFX** ou **Money**
- Tente com um período menor (ex: 1 mês)

---

### Categorização muito lenta

**Causa:** Modelo LLM muito pesado para seu hardware

**Solução:**
```bash
# Usar modelo mais leve
ollama pull phi

# No dashboard, selecione "phi" no seletor de modelo
```

---

### Padrões não estão sendo salvos

**Causa:** Permissões de escrita na pasta `data/`

**Solução:**
```bash
# Criar pasta manualmente
mkdir data

# Dar permissões (Linux/macOS)
chmod 755 data
```

---

## 📊 Exemplos de Uso

### Análise Mensal

1. Faça upload do extrato de 1 mês
2. Categorize com LLM
3. Vá em **Visão Geral** → veja gráfico de tendência mensal
4. Compare receitas vs despesas

### Identificar Maiores Gastos

1. Vá em **Análises**
2. Veja **Top 10 Maiores Despesas**
3. Identifique onde está gastando mais
4. Ajuste seus hábitos

### Exportar para Excel

1. Vá em **Transações**
2. Aplique filtros desejados
3. Clique em **📥 Download CSV**
4. Abra no Excel para análises customizadas

### Comparar Categorias

1. Vá em **Visão Geral**
2. Veja gráfico de pizza
3. Identifique categorias que mais pesam
4. Planeje cortes ou ajustes

---

## 🎯 Próximas Funcionalidades

- [ ] Suporte a múltiplos arquivos OFX simultâneos
- [ ] Comparação entre meses/períodos
- [ ] Alertas de gastos acima da média
- [ ] Orçamento por categoria
- [ ] Previsão de gastos futuros com ML
- [ ] Export para PDF com relatórios
- [ ] Sincronização automática com bancos (Open Banking)
- [ ] App mobile (PWA)

---

## 🔒 Privacidade e Segurança

- ✅ **100% Local:** Todos os dados ficam no seu computador
- ✅ **Sem Internet:** LLM roda localmente via Ollama
- ✅ **Sem Cadastro:** Não precisa criar conta
- ✅ **Sem Uploads Externos:** Arquivos OFX não saem da sua máquina
- ✅ **Open Source:** Código totalmente auditável

---

## 📄 Licença

Este projeto está disponível sob a licença **MIT**.

---

## 👨‍💻 Autor

**Jordan Arruda**  
- GitHub: [@Juerda](https://github.com/Juerda)
- Blog: [blog-dados.vercel.app](https://blog-dados.vercel.app)

---

## 🙏 Agradecimentos

- **Ollama** - Por tornar LLMs locais tão fáceis
- **Streamlit** - Pela framework web incrível
- **ofxparse** - Pela biblioteca de parsing OFX
- **Plotly** - Pelos gráficos interativos

---

## 🆘 Suporte

Encontrou um problema ou tem uma sugestão?

- 🐛 **Bug:** Abra uma issue no GitHub
- 💡 **Sugestão:** Abra uma discussion no GitHub
- 📧 **Contato:** jordansales.arruda@gmail.com

---

<div align="center">

**⭐ Se este projeto foi útil, considere dar uma estrela! ⭐**

**💰 Desenvolvido com ❤️ para controle financeiro pessoal 💰**

---

*Última atualização: Dezembro 2025*

</div>
