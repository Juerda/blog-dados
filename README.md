# 📊 Blog de Dados - Jordan Arruda

> Blog profissional sobre análise de dados, Python e tecnologia construído com Pelican (gerador de sites estáticos em Python)

[![Vercel](https://img.shields.io/badge/Vercel-Deployed-success?logo=vercel)](https://vercel.com)
[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)](https://www.python.org/)
[![Pelican](https://img.shields.io/badge/Pelican-4.9+-orange?logo=pelican)](https://getpelican.com/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## 🌟 Características Principais

- ✅ **100% Python** - Construído com Pelican, sem dependências de Node.js
- 📱 **Totalmente Responsivo** - Design mobile-first otimizado para todos os dispositivos
- 🎨 **Design Moderno** - Interface profissional com tema claro/escuro automático
- 💬 **Sistema de Comentários** - Integração com Giscus (autenticação via GitHub)
- 🔗 **Compartilhamento Social** - Botões para Twitter, LinkedIn, Facebook e WhatsApp
- 📊 **Gráficos Interativos** - Suporte a visualizações de dados com Canvas API
- 📥 **Export de Dados** - Download de dados em CSV diretamente dos gráficos
- 🔍 **SEO Otimizado** - URLs limpas, meta tags, sitemap XML, feeds RSS/Atom
- ⚡ **Performance Máxima** - Site estático puro, carregamento instantâneo
- 🎯 **Banners SVG Personalizados** - Ilustrações profissionais por categoria
- 🌙 **Tema Claro/Escuro** - Alternância suave com persistência no localStorage
- 🚀 **Deploy Automático** - Integração completa com Vercel

---

## 📑 Índice

1. [Início Rápido](#-início-rápido)
2. [Pré-requisitos](#-pré-requisitos)
3. [Instalação Passo a Passo](#-instalação-passo-a-passo)
4. [Estrutura do Projeto](#-estrutura-do-projeto)
5. [Como Criar Conteúdo](#-como-criar-conteúdo)
6. [Funcionalidades Avançadas](#-funcionalidades-avançadas)
7. [Personalização](#-personalização)
8. [Deploy e Publicação](#-deploy-e-publicação)
9. [Comandos Úteis](#-comandos-úteis)
10. [Solução de Problemas](#-solução-de-problemas)
11. [Recursos e Documentação](#-recursos-e-documentação)

---

## 🚀 Início Rápido

Para usuários experientes que querem começar imediatamente:

```bash
# 1. Clone o repositório
git clone https://github.com/Juerda/blog-dados.git
cd blog-dados

# 2. Crie ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # macOS/Linux

# 3. Instale dependências
pip install -r requirements.txt

# 4. Gere o site
python -m pelican content -o output -s pelicanconf.py

# 5. Sincronize arquivos estáticos
python sync_theme.py

# 6. Execute servidor local
python -m http.server 8000 -d output
```

Acesse: **http://localhost:8000**

---

## 📋 Pré-requisitos

Antes de começar, certifique-se de ter instalado:

| Software | Versão Mínima | Download | Verificar Instalação |
|----------|---------------|----------|---------------------|
| **Python** | 3.8+ | [python.org](https://www.python.org/downloads/) | `python --version` |
| **pip** | 20.0+ | (incluído com Python) | `pip --version` |
| **Git** | 2.0+ | [git-scm.com](https://git-scm.com/) | `git --version` |

### Verificação Rápida

```bash
# Verifique se tudo está instalado corretamente
python --version    # Deve mostrar: Python 3.8.x ou superior
pip --version       # Deve mostrar: pip 20.x ou superior
git --version       # Deve mostrar: git version 2.x
```

---

## 🛠️ Instalação Passo a Passo

### Passo 1: Obter o Código

**Opção A: Clonar o repositório (recomendado)**
```bash
git clone https://github.com/Juerda/blog-dados.git
cd blog-dados
```

**Opção B: Download manual**
1. Baixe o ZIP do repositório no GitHub
2. Extraia para uma pasta de sua escolha
3. Navegue até a pasta no terminal

---

### Passo 2: Criar Ambiente Virtual

O ambiente virtual isola as dependências do projeto.

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

> 💡 **Dica:** Quando o ambiente estiver ativo, você verá `(venv)` no início da linha do terminal.

---

### Passo 3: Instalar Dependências

```bash
pip install -r requirements.txt
```

**Dependências incluídas:**
- `pelican[markdown]==4.9.1` - Gerador de sites estáticos
- `markdown` - Processamento de Markdown
- `typogrify` - Melhorias tipográficas
- `beautifulsoup4` - Parsing HTML

---

### Passo 4: Gerar o Site

```bash
python -m pelican content -o output -s pelicanconf.py
```

Este comando:
- ✅ Lê todos os arquivos `.md` da pasta `content/`
- ✅ Processa templates Jinja2 da pasta `theme/`
- ✅ Gera HTML estático na pasta `output/`

---

### Passo 5: Sincronizar Arquivos Estáticos

```bash
python sync_theme.py
```

Este script copia arquivos CSS, JavaScript e imagens para a pasta de output.

---

### Passo 6: Visualizar Localmente

**Opção A: Servidor Python simples**
```bash
python -m http.server 8000 -d output
```

**Opção B: Servidor Pelican com auto-reload**
```bash
pelican -l -r content -o output -s pelicanconf.py
```

Acesse em seu navegador: **http://localhost:8000**

> 🎉 **Pronto!** Seu blog está rodando localmente.

---

## 📂 Estrutura do Projeto

```
blog-dados/
│
├── 📁 content/                    # Conteúdo do site (posts e páginas)
│   ├── 📄 *.md                   # Posts do blog (arquivos Markdown)
│   └── 📁 pages/                 # Páginas estáticas
│       └── sobre.md              # Página "Sobre"
│
├── 📁 theme/                      # Tema customizado do site
│   ├── 📁 templates/             # Templates Jinja2
│   │   ├── base.html            # Template base (header, footer, scripts)
│   │   ├── index.html           # Homepage (últimos 3 posts)
│   │   ├── article.html         # Template de artigo individual
│   │   ├── archives.html        # Página do blog (todos os posts)
│   │   └── page.html            # Template de páginas estáticas
│   │
│   └── 📁 static/                # Arquivos estáticos
│       ├── 📁 css/
│       │   └── style.css        # Estilos principais (1470+ linhas)
│       ├── 📁 js/
│       │   ├── main.js          # Theme toggle e menu mobile
│       │   └── pie-chart.js     # Gráficos de pizza interativos
│       └── 📁 images/
│           └── profile.jpg      # Foto de perfil
│
├── 📁 output/                     # Site gerado (criado após build)
│   └── ...                       # HTML, CSS, JS prontos para deploy
│
├── 📄 pelicanconf.py             # Configurações principais do Pelican
├── 📄 requirements.txt           # Dependências Python
├── 📄 sync_theme.py              # Script para sincronizar arquivos estáticos
├── 📄 vercel.json                # Configuração para deploy no Vercel
├── 📄 .gitignore                 # Arquivos ignorados pelo Git
└── 📄 README.md                  # Esta documentação
```

### Descrição dos Arquivos Principais

| Arquivo | Descrição |
|---------|-----------|
| `pelicanconf.py` | Configurações do site (nome, autor, timezone, URLs, ordenação) |
| `sync_theme.py` | Copia CSS/JS/imagens para output (executar após cada build) |
| `requirements.txt` | Lista de pacotes Python necessários |
| `vercel.json` | Configuração de build e deploy para Vercel |

---

## 📝 Como Criar Conteúdo

### Criando um Novo Post

1. **Crie um arquivo Markdown** na pasta `content/`
   - Nome sugerido: `YYYY-MM-DD-titulo-do-post.md`
   - Exemplo: `2025-12-11-introducao-python.md`

2. **Adicione o cabeçalho (frontmatter)**

```markdown
Title: Título do Seu Post
Date: 2025-12-11 10:30
Category: Python
Tags: python, dados, tutorial
Slug: introducao-python
Summary: Breve resumo que aparece nas listagens
Author: Jordan Arruda

Aqui começa o conteúdo do seu post...
```

### Campos do Frontmatter

| Campo | Obrigatório | Descrição | Exemplo |
|-------|-------------|-----------|---------|
| `Title` | ✅ Sim | Título do artigo | `Análise de Dados com Python` |
| `Date` | ✅ Sim | Data de publicação | `2025-12-11` ou `2025-12-11 14:30` |
| `Category` | ✅ Sim | Categoria (Python, E-commerce, Tecnologia) | `Python` |
| `Tags` | ✅ Sim | Tags separadas por vírgula | `python, dados, análise` |
| `Slug` | ✅ Sim | URL amigável (sem espaços, use hífens) | `analise-dados-python` |
| `Summary` | ⚪ Opcional | Resumo breve para listagens | `Aprenda a analisar dados...` |
| `Author` | ⚪ Opcional | Nome do autor | `Jordan Arruda` |

---

### Exemplo Completo de Post

````markdown
Title: Como Analisar Dados de E-commerce com Python
Date: 2025-12-11 15:00
Category: Python
Tags: python, e-commerce, análise, pandas
Slug: analisar-dados-ecommerce-python
Summary: Tutorial completo sobre análise de dados de vendas online usando Python e Pandas

# Introdução

Neste artigo, vamos aprender como analisar dados de e-commerce usando Python.

## O que vamos construir

Vamos criar um script que:

1. Importa dados de vendas
2. Limpa e processa os dados
3. Gera visualizações interativas
4. Exporta relatórios em CSV

## Passo 1: Importar Bibliotecas

```python
import pandas as pd
import matplotlib.pyplot as plt

# Carregar dados
df = pd.read_csv('vendas.csv')
```

## Conclusão

Com Python, análise de dados fica muito mais fácil!
````

---

### Criando Páginas Estáticas

Páginas (como "Sobre", "Contato") vão na pasta `content/pages/`:

```markdown
Title: Sobre
Date: 2025-12-11
Slug: sobre

# Sobre o Blog

Este blog é dedicado a análise de dados, Python e tecnologia.

## Minhas Especialidades

- Python e análise de dados
- Visualização de dados
- Machine Learning
- E-commerce Analytics
```

---

### Sintaxe Markdown Suportada

| Elemento | Sintaxe | Resultado |
|----------|---------|-----------|
| **Negrito** | `**texto**` | **texto** |
| *Itálico* | `*texto*` | *texto* |
| `Código inline` | `` `código` `` | `código` |
| [Link](url) | `[texto](url)` | Link clicável |
| ![Imagem](url) | `![alt](url)` | Imagem |
| Título H2 | `## Título` | Título grande |
| Título H3 | `### Título` | Título médio |
| Lista | `- item` | • item |
| Lista numerada | `1. item` | 1. item |
| Citação | `> texto` | Texto citado |
| Linha horizontal | `---` | Linha |
| Bloco de código | ` ```python ` | Código destacado |

---

## 🎯 Funcionalidades Avançadas

### 1. Sistema de Comentários (Giscus)

Os comentários são gerenciados pelo **Giscus**, que usa GitHub Discussions.

**Como funciona:**
1. ✅ Usuários fazem login com conta GitHub
2. ✅ Comentam diretamente no artigo
3. ✅ Comentários ficam armazenados no GitHub Discussions
4. ✅ Suporte a reações (👍, ❤️, 🎉, etc)
5. ✅ Tema automático (claro/escuro seguindo o site)

**Configuração atual:**
- Repositório: `Juerda/blog-dados`
- Categoria: General
- Tema: `preferred_color_scheme` (automático)
- Idioma: Português (pt)
- **Autenticação:** Apenas GitHub (obrigatório pelo sistema)

> ℹ️ **Nota sobre autenticação:** O Giscus usa exclusivamente autenticação GitHub, pois os comentários são armazenados no GitHub Discussions. Não há suporte nativo para Google, Facebook ou outras redes sociais. Se precisar de múltiplos provedores de login, considere alternativas como Disqus, Commento ou Hyvor Talk (porém são pagos ou com limitações).

**Para personalizar:**
1. Acesse: https://giscus.app/
2. Configure suas preferências
3. Copie o código gerado
4. Cole em `theme/templates/article.html` na seção `<!-- Comments Section -->`

---

### 2. Compartilhamento Social

Cada artigo inclui botões de compartilhamento para 4 redes sociais:

| Rede Social | Cor | Funcionalidade |
|-------------|-----|----------------|
| **Twitter** | Azul claro (#1DA1F2) | Tweet com título + link |
| **LinkedIn** | Azul escuro (#0A66C2) | Post profissional |
| **Facebook** | Azul royal (#1877F2) | Compartilhamento no feed |
| **WhatsApp** | Verde (#25D366) | Envio direto por mensagem |

**Onde aparece:** Logo após o conteúdo do artigo, antes das tags.

**Funcionalidades:**
- ✅ URLs com encoding correto
- ✅ Abre em nova aba
- ✅ Efeito hover com elevação
- ✅ Sombras coloridas
- ✅ Ícones SVG customizados
- ✅ Responsivo (empilha no mobile)

**Personalizar cores:**
Edite `theme/static/css/style.css` na seção `/* Social Share Section */`

---

### 3. Gráficos Interativos (Pie Charts)

O blog suporta gráficos de pizza interativos com export CSV.

**Como adicionar um gráfico:**

```html
<!-- No seu post .md -->
<div class="pie-chart-container" id="meuGrafico">
    <canvas class="pie-chart-canvas"></canvas>
    <button class="download-csv">Download CSV</button>
</div>

<script>
(function() {
    const chart = new PieChart('meuGrafico', {
        'Categoria A': 40,
        'Categoria B': 30,
        'Categoria C': 20,
        'Categoria D': 10
    });
    chart.draw();
    
    // Registrar para export CSV
    window.pieCharts = window.pieCharts || {};
    window.pieCharts.meuGrafico = {
        getData: () => chart.data
    };
})();
</script>
```

**Funcionalidades:**
- ✅ Rendering em alta resolução (DPI scaling)
- ✅ Cores automáticas variadas
- ✅ Legendas com percentuais
- ✅ Export para CSV com um clique
- ✅ Fundo branco para visibilidade
- ✅ Responsivo (adapta ao container)

**Exemplos no blog:**
- `2024-12-08-tendencias-ecommerce-google-trends.md` → Gráfico de categorias
- `2024-11-25-coletar-processar-dados-python.md` → Gráfico de métodos

---

### 4. Tema Claro/Escuro

O site possui alternância automática entre tema claro e escuro.

**Como funciona:**
- ✅ Botão no canto superior direito (sol/lua)
- ✅ Preferência salva em `localStorage`
- ✅ Ícones SVG customizados (12 raios no sol, crescente na lua)
- ✅ Transição suave entre temas (0.3s)
- ✅ Rotação animada do ícone (360deg)

**Cores dos temas:**

| Elemento | Tema Claro | Tema Escuro |
|----------|------------|-------------|
| Background | #FFFFFF | #051428 |
| Texto | #1A2332 | #F3F4F6 |
| Primary | #0066CC | #00AEFF |
| Navbar | #FFFFFF | #0A2342 |
| Footer | #0066CC | #051428 |
| Border | #E5E7EB | #1E3A5F |

**Personalizar:**
Edite as variáveis CSS em `theme/static/css/style.css`:

```css
/* Tema Claro */
:root, :root[data-theme="light"] {
    --primary-blue: #0066CC;
    --bg-primary: #FFFFFF;
    --text-primary: #1A2332;
    --border-color: #E5E7EB;
}

/* Tema Escuro */
:root[data-theme="dark"] {
    --primary-blue: #00AEFF;
    --bg-primary: #051428;
    --text-primary: #F3F4F6;
    --border-color: #1E3A5F;
}
```

---

### 5. Banners SVG por Categoria

Cada categoria tem um banner SVG único e profissional no topo dos artigos:

| Categoria | Design | Cores | Ícones |
|-----------|--------|-------|--------|
| **E-commerce** | Moderno e comercial | Laranja (#FF6B35) → Vermelho (#D32F2F) | Carrinho + gráfico + moedas |
| **Python** | Tech e coding | Azul (#00A8E8) → Ciano (#00C9FF) | Logo Python + brackets |
| **Tecnologia** | Inovação | Roxo (#7B2CBF) → Roxo escuro (#5A189A) | Microchip + foguete + ondas |
| **Default** | Conhecimento | Azul (#0066CC) → Azul escuro (#003D7A) | Livro + estrelas |

**Dimensões:** 1200x300px (viewBox responsivo)

**Personalizar banners:**
Edite `theme/templates/article.html` nas seções de SVG (linhas 8-185).

---

## ⚙️ Personalização

### Configurações do Site

Edite `pelicanconf.py` para personalizar informações básicas:

```python
# Informações básicas
AUTHOR = 'Jordan Arruda'
SITENAME = 'Blog de Dados'
SITEURL = ''  # Vercel preencherá automaticamente
TIMEZONE = 'America/Sao_Paulo'
DEFAULT_LANG = 'pt'

# Ordenação de artigos
ARTICLE_ORDER_BY = 'date'
REVERSE_ARTICLE_ORDER = True  # Mais recentes primeiro

# URLs
ARTICLE_URL = '{slug}.html'
ARTICLE_SAVE_AS = '{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
ARCHIVES_SAVE_AS = 'blog.html'

# Templates
DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'archives']
DEFAULT_PAGINATION = False  # Sem paginação
```

---

### Alterar Cores e Estilos

Todas as cores do site estão centralizadas em variáveis CSS.

**Localização:** `theme/static/css/style.css` (linhas 1-130)

**Exemplo - Mudar cor primária:**

```css
:root, :root[data-theme="light"] {
    --primary-blue: #FF5722;  /* Era #0066CC, agora é laranja */
}

:root[data-theme="dark"] {
    --primary-blue: #FF7043;  /* Laranja mais claro no escuro */
}
```

**Principais variáveis:**

```css
/* Cores */
--primary-blue: cor principal do site
--bg-primary: fundo principal
--bg-secondary: fundo secundário (cards, seções)
--bg-nav: fundo da navbar
--text-primary: texto principal
--text-secondary: texto secundário
--border-color: cor das bordas

/* Espaçamento */
--spacing-xs: 0.25rem
--spacing-sm: 0.5rem
--spacing-md: 1rem
--spacing-lg: 1.5rem
--spacing-xl: 2rem
--spacing-2xl: 3rem
--spacing-3xl: 4rem

/* Tipografia */
--font-size-xs: 0.75rem
--font-size-sm: 0.875rem
--font-size-base: 1rem
--font-size-lg: 1.125rem
--font-size-xl: 1.25rem
--font-size-2xl: 1.5rem
--font-size-3xl: 1.875rem
--font-size-4xl: 2.25rem

/* Bordas */
--radius-sm: 0.25rem
--radius-md: 0.5rem
--radius-lg: 1rem
--radius-full: 9999px
```

---

### Personalizar Menu de Navegação

O menu é renderizado automaticamente, mas você pode customizar links extras.

**Editar:** `theme/templates/base.html` (linha ~40)

```html
<nav class="navbar-menu">
    <a href="/">Home</a>
    <a href="/blog.html">Blog</a>
    <a href="/sobre.html">Sobre</a>
    <!-- Adicione mais links aqui -->
    <a href="/contato.html">Contato</a>
    <a href="/portfolio.html">Portfolio</a>
</nav>
```

---

### Alterar Links Sociais no Rodapé

**Editar:** `theme/templates/base.html` (seção footer, ~linha 75)

```html
<div class="social-links">
    <a href="https://github.com/Juerda" target="_blank" aria-label="GitHub">
        <i class="fab fa-github"></i>
    </a>
    <a href="https://linkedin.com/in/seu-perfil" target="_blank" aria-label="LinkedIn">
        <i class="fab fa-linkedin"></i>
    </a>
    <a href="https://twitter.com/seu-usuario" target="_blank" aria-label="Twitter">
        <i class="fab fa-twitter"></i>
    </a>
    <!-- Adicione mais redes aqui -->
</div>
```

---

### Adicionar Favicon

1. Coloque seu `favicon.ico` em `theme/static/images/`
2. Adicione em `theme/templates/base.html` (dentro de `<head>`):

```html
<link rel="icon" type="image/x-icon" href="/theme/static/images/favicon.ico">
```

---

### Alterar Fonte do Site

**Opção A: Google Fonts**

Em `theme/templates/base.html` (dentro de `<head>`):

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">
```

Em `theme/static/css/style.css`:

```css
:root {
    --font-body: 'Inter', sans-serif;
}

body {
    font-family: var(--font-body);
}
```

---

## 🚀 Deploy e Publicação

### Deploy no Vercel (Recomendado)

**Passo 1: Preparar Repositório GitHub**

```bash
# Inicializar Git (se ainda não fez)
git init
git add .
git commit -m "Initial commit: Blog de Dados"

# Criar repositório no GitHub (via web)
# Depois conectar:
git remote add origin https://github.com/Juerda/blog-dados.git
git branch -M main
git push -u origin main
```

**Passo 2: Conectar ao Vercel**

1. Acesse [vercel.com](https://vercel.com) e faça login
2. Clique em **"New Project"**
3. Selecione seu repositório `blog-dados`
4. Vercel detectará automaticamente `vercel.json`
5. Clique em **"Deploy"**

**Passo 3: Aguardar Build**

O Vercel executará automaticamente:
```bash
pip install -r requirements.txt
python -m pelican content -o output -s pelicanconf.py
```

**Passo 4: Acessar Site**

Após deploy (1-2 minutos), seu site estará em:
- `https://blog-dados.vercel.app` (ou nome que você escolheu)

---

### Deploy Manual com Vercel CLI

```bash
# Instalar Vercel CLI
npm install -g vercel

# Fazer login
vercel login

# Deploy para preview
vercel

# Deploy para produção
vercel --prod
```

---

### Deploy em Outras Plataformas

**Netlify:**
1. Conecte repositório GitHub
2. Build command: `pip install -r requirements.txt && pelican content -o output -s pelicanconf.py`
3. Publish directory: `output`

**GitHub Pages:**
```bash
# Instalar ghp-import
pip install ghp-import

# Gerar site
pelican content -o output -s pelicanconf.py

# Publicar
ghp-import -m "Update site" -b gh-pages output
git push origin gh-pages
```

---

### Conectar Domínio Customizado

**No Vercel:**
1. Vá em **Settings** → **Domains**
2. Adicione seu domínio (ex: `www.seublog.com`)
3. Configure DNS no registrador do domínio:
   - Tipo: `CNAME`
   - Nome: `www`
   - Valor: `cname.vercel-dns.com`

---

### Configurar SITEURL para Produção

Após deploy, edite `pelicanconf.py`:

```python
SITEURL = 'https://blog-dados.vercel.app'  # Ou seu domínio customizado
```

Recompile e faça novo deploy.

---

## 🔧 Comandos Úteis

### Comandos Pelican

```bash
# Gerar site uma vez
python -m pelican content -o output -s pelicanconf.py

# Gerar com servidor local e auto-reload
pelican -l -r content -o output -s pelicanconf.py

# Limpar pasta output antes de gerar
pelican content -o output -s pelicanconf.py --delete-output-directory

# Ver versão do Pelican
pelican --version
```

---

### Comandos de Sincronização

```bash
# Sincronizar arquivos estáticos (CSS, JS, imagens)
python sync_theme.py

# Workflow completo (gerar + sincronizar)
python -m pelican content -o output -s pelicanconf.py ; python sync_theme.py
```

---

### Comandos Git

```bash
# Ver status das mudanças
git status

# Adicionar todos os arquivos
git add .

# Fazer commit
git commit -m "Adicionar novo post sobre Python"

# Enviar para GitHub
git push origin main

# Ver histórico de commits
git log --oneline

# Criar nova branch
git checkout -b nova-feature
```

---

### Gerenciamento de Dependências

```bash
# Instalar nova dependência
pip install nome-do-pacote

# Atualizar requirements.txt
pip freeze > requirements.txt

# Instalar todas as dependências
pip install -r requirements.txt

# Atualizar Pelican
pip install --upgrade pelican
```

---

### Servidor Local

```bash
# Servidor Python simples
python -m http.server 8000 -d output

# Servidor Pelican com reload automático
pelican -l -r content -o output -s pelicanconf.py

# Acessar de outro dispositivo na rede
python -m http.server 8000 -d output --bind 0.0.0.0
# Depois acesse: http://SEU_IP:8000
```

---

## 🐛 Solução de Problemas

### Posts não aparecem no site

**Causa:** Erro no frontmatter do arquivo `.md`

**Solução:**
1. Verifique se o arquivo está em `content/`
2. Confirme que todos os campos obrigatórios existem:
   ```markdown
   Title: Título
   Date: 2025-12-11
   Category: Python
   Tags: python, dados
   Slug: titulo-do-post
   ```
3. Certifique-se de que a data não é futura
4. Regere o site: `python -m pelican content -o output -s pelicanconf.py`

---

### CSS não carrega ou está desatualizado

**Causa:** Arquivos estáticos não foram sincronizados

**Solução:**
```bash
# Sincronizar arquivos estáticos
python sync_theme.py

# Limpar cache do navegador
Ctrl + Shift + Delete (Chrome/Edge)
Cmd + Shift + Delete (macOS)

# Forçar recarga sem cache
Ctrl + F5 (Windows)
Cmd + Shift + R (macOS)
```

---

### Gráficos de pizza não aparecem

**Causa:** Script não executado ou erro no JavaScript

**Solução:**
1. Verifique se `pie-chart.js` está carregando (Console do navegador F12)
2. Confirme que o script está completo no arquivo `.md`:
   ```html
   <script>
   (function() {
       const chart = new PieChart('meuGrafico', {...});
       chart.draw();
       window.pieCharts = window.pieCharts || {};
       window.pieCharts.meuGrafico = {
           getData: () => chart.data
       };
   })();
   </script>
   ```
3. Certifique-se de que `sync_theme.py` foi executado

---

### Comentários Giscus não aparecem

**Causa:** GitHub Discussions não habilitado ou configuração incorreta

**Solução:**
1. No GitHub, vá em **Settings** → **General**
2. Role até **Features** e habilite **Discussions**
3. Verifique se `data-repo` em `article.html` está correto:
   ```html
   data-repo="Juerda/blog-dados"
   ```
4. Confirme que o repositório é público

---

### Erro ao fazer deploy no Vercel

**Causa:** Configuração incorreta ou dependências faltando

**Solução:**
1. Verifique se `vercel.json` existe na raiz do projeto
2. Confirme que `requirements.txt` está atualizado
3. Veja os logs do Vercel para erro específico
4. Teste o build localmente:
   ```bash
   pip install -r requirements.txt
   python -m pelican content -o output -s pelicanconf.py
   ```

---

### Tema claro/escuro não persiste

**Causa:** localStorage bloqueado ou JavaScript desabilitado

**Solução:**
1. Verifique se JavaScript está habilitado no navegador
2. Limpe cookies e dados do site
3. Teste em modo anônimo
4. Verifique Console (F12) por erros em `main.js`

---

### Ambiente virtual não ativa (Windows)

**Causa:** Política de execução do PowerShell

**Solução:**
```powershell
# Executar como Administrador:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Depois ativar ambiente:
venv\Scripts\activate
```

---

## 📚 Recursos e Documentação

### Documentação Oficial

| Ferramenta | Link | Descrição |
|------------|------|-----------|
| **Pelican** | [docs.getpelican.com](https://docs.getpelican.com/) | Gerador de sites estáticos |
| **Markdown** | [markdownguide.org](https://www.markdownguide.org/) | Sintaxe Markdown completa |
| **Jinja2** | [jinja.palletsprojects.com](https://jinja.palletsprojects.com/) | Engine de templates |
| **Vercel** | [vercel.com/docs](https://vercel.com/docs) | Deploy e hospedagem |
| **Giscus** | [giscus.app](https://giscus.app/) | Sistema de comentários |

---

### Tutoriais Úteis

- [Como escrever bons posts técnicos](https://www.freecodecamp.org/news/technical-writing/)
- [SEO para blogs](https://moz.com/beginners-guide-to-seo)
- [Git e GitHub para iniciantes](https://www.freecodecamp.org/news/git-and-github-for-beginners/)
- [Python para análise de dados](https://pandas.pydata.org/docs/user_guide/index.html)

---

### Ferramentas Recomendadas

| Ferramenta | Uso | Link |
|------------|-----|------|
| **VS Code** | Editor de código | [code.visualstudio.com](https://code.visualstudio.com/) |
| **GitHub Desktop** | Interface Git visual | [desktop.github.com](https://desktop.github.com/) |
| **TinyPNG** | Comprimir imagens | [tinypng.com](https://tinypng.com/) |
| **Carbon** | Screenshots de código | [carbon.now.sh](https://carbon.now.sh/) |
| **Grammarly** | Revisar textos | [grammarly.com](https://grammarly.com/) |

---

### Extensões VS Code Recomendadas

```json
{
  "recommendations": [
    "ms-python.python",           // Suporte Python
    "streetsidesoftware.code-spell-checker",  // Corretor ortográfico
    "yzhang.markdown-all-in-one", // Ferramentas Markdown
    "esbenp.prettier-vscode",     // Formatador de código
    "ms-vscode.live-server"       // Servidor local
  ]
}
```

---

### Comunidade e Suporte

- **GitHub Issues**: [github.com/Juerda/blog-dados/issues](https://github.com/Juerda/blog-dados/issues)
- **Pelican Community**: [github.com/getpelican/pelican/discussions](https://github.com/getpelican/pelican/discussions)
- **Stack Overflow**: Tag `pelican` ou `static-site-generator`

---

## 📊 Funcionalidades Implementadas

- [x] Homepage com últimos 3 posts
- [x] Página de blog com todos os posts ordenados
- [x] Posts individuais com navegação anterior/próximo
- [x] Página "Sobre" com foto de perfil
- [x] Design 100% responsivo (mobile, tablet, desktop)
- [x] Tema claro/escuro com alternância manual
- [x] Banners SVG personalizados por categoria
- [x] Sistema de comentários via Giscus (GitHub)
- [x] Botões de compartilhamento social (4 redes)
- [x] Gráficos de pizza interativos com Canvas
- [x] Export de dados em CSV
- [x] Feed RSS/Atom automático
- [x] Sitemap XML para SEO
- [x] Menu mobile responsivo
- [x] Botão "Voltar ao Blog/Home"
- [x] Tags e categorias funcionais
- [x] URLs amigáveis (slugs limpos)
- [x] Deploy automático no Vercel

---

## 🎨 Próximas Melhorias (Roadmap)

### Curto Prazo
- [ ] Sistema de busca no site
- [ ] Página de arquivo por categoria
- [ ] Página de arquivo por tags
- [ ] Newsletter com formulário de inscrição
- [ ] Analytics (Google Analytics ou Plausible)

### Médio Prazo
- [ ] Modo leitura (reader mode)
- [ ] Tempo estimado de leitura
- [ ] Tabela de conteúdos automática
- [ ] Relacionados (posts similares)
- [ ] Galeria de imagens com lightbox

### Longo Prazo
- [ ] Suporte a múltiplos autores
- [ ] Sistema de séries/tutoriais
- [ ] Modo offline (PWA)
- [ ] Integração com CMS headless
- [ ] API para consultar posts

---

## 📄 Licença

Este projeto está disponível sob a licença **MIT**. Você é livre para:

- ✅ Usar comercialmente
- ✅ Modificar o código
- ✅ Distribuir
- ✅ Uso privado

**Condições:**
- Manter aviso de copyright e licença

---

## ✨ Créditos

**Desenvolvido por:** Jordan Arruda  
**Tecnologia:** Pelican (Python)  
**Deploy:** Vercel  
**Comentários:** Giscus (GitHub Discussions)  
**Ícones:** Font Awesome + SVG customizados  

---

## 📞 Contato

- **GitHub**: [@Juerda](https://github.com/Juerda)
- **LinkedIn**: [Jordan Arruda](https://linkedin.com/in/seu-perfil)
- **E-mail**: seu-email@exemplo.com
- **Site**: [blog-dados.vercel.app](https://blog-dados.vercel.app)

---

## 🙏 Agradecimentos

- Comunidade Pelican pelo excelente gerador de sites
- Giscus por tornar comentários tão simples
- Vercel pela hospedagem gratuita e rápida
- Font Awesome pelos ícones
- Você por usar este projeto! 🎉

---

<div align="center">

**⭐ Se este projeto foi útil, considere dar uma estrela no GitHub! ⭐**

**📚 Criado com ❤️ para entusiastas de dados e Python 📚**

---

*Última atualização: Dezembro 2025*

</div>
