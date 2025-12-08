# Blog de Dados - Site Estático com Python

Um blog estático responsivo criado com **Pelican** (gerador de sites estáticos em Python), pronto para deploy no Vercel.

## 🚀 Características

- ✅ **100% Python** - Construído com Pelican, sem dependências de Node.js
- 📱 **Responsivo** - Design mobile-first que funciona em qualquer dispositivo
- 🎨 **Tema Customizável** - Template Jinja2 moderno e limpo
- 🔍 **SEO Otimizado** - URLs limpas, feed RSS/Atom, sitemap XML
- ⚡ **Rápido** - Site estático puro, sem banco de dados
- 🚀 **Pronto para Vercel** - Configuração incluída para deploy automático

## 📋 Pré-requisitos

- Python 3.8+
- pip (gerenciador de pacotes Python)
- Git (para versionamento)

## 🛠️ Instalação Local

### 1. Clonar ou baixar o repositório

```bash
cd "Projeto - Blog"
```

### 2. Criar e ativar um ambiente virtual (recomendado)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Gerar o site

```bash
pelican content -o output -s pelicanconf.py
```

### 5. Visualizar localmente

```bash
# Usando Python 3
python -m http.server 8000 -d output

# Ou usando Pelican com servidor autoreload
pelican -l -r content -o output -s pelicanconf.py
```

Acesse: `http://localhost:8000`

## 📝 Como Criar Posts

### Formato: Markdown

Crie um novo arquivo `.md` na pasta `content/` com o seguinte formato:

```markdown
Title: Seu Título Aqui
Date: 2024-12-08
Category: Categoria
Tags: tag1, tag2, tag3
Slug: seu-slug-aqui

Aqui começa o conteúdo do seu post em Markdown...

## Seção 1

Você pode usar toda a sintaxe Markdown padrão:

- Listas
- **Negrito**
- *Itálico*
- [Links](https://exemplo.com)
- Código inline e blocos

```python
# Blocos de código
def hello():
    print("Olá!")
```

### Seção aninhada

E muito mais!
```

### Campos obrigatórios:

- **Title**: Título do seu artigo
- **Date**: Data de publicação (formato: YYYY-MM-DD)
- **Category**: Categoria do post
- **Tags**: Tags separadas por vírgula
- **Slug**: URL-friendly do post (use hífens, sem espaços)

### Exemplo completo:

```markdown
Title: Análise de Dados com Python
Date: 2024-12-08
Category: Python
Tags: análise, dados, python
Slug: analise-dados-python

# Introdução

Este é um exemplo de post com análise de dados...

## Seção importante

Conteúdo aqui...
```

## 📂 Estrutura do Projeto

```
├── content/              # Seus posts em Markdown
│   ├── posts/           # Posts do blog
│   └── pages/           # Páginas estáticas (Sobre, etc)
├── theme/               # Tema do site
│   ├── templates/       # Templates Jinja2
│   └── static/          # CSS, JS, imagens
├── output/              # Site gerado (criado após build)
├── pelicanconf.py       # Configurações principais
├── requirements.txt     # Dependências Python
├── vercel.json          # Configuração Vercel
└── README.md            # Este arquivo
```

## ⚙️ Personalizar o Blog

### Informações do Site

Edite `pelicanconf.py`:

```python
AUTHOR = 'Seu Nome'
SITENAME = 'Título do Seu Blog'
SITEURL = ''  # URL final (Vercel preencherá)
TIMEZONE = 'America/Sao_Paulo'
```

### Cores e Estilos

Edite `theme/static/css/style.css` e modifique as variáveis CSS:

```css
:root {
    --primary-color: #2c3e50;      /* Cor principal */
    --secondary-color: #3498db;    /* Cor secundária */
    --accent-color: #e74c3c;       /* Cor de destaque */
    /* ... mais variáveis ... */
}
```

### Menu de Navegação

Em `pelicanconf.py`, customize:

```python
MENUITEMS = (
    ('Home', '/'),
    ('Blog', '/blog/'),
    ('Sobre', '/sobre/'),
    ('Contato', '/contato/'),
)
```

### Links Sociais

Em `theme/templates/base.html`, localize a seção de redes sociais e atualize os links:

```html
<a href="https://github.com/seu-usuario" target="_blank">
    <i class="fab fa-github"></i>
</a>
```

## 🚀 Deploy no Vercel

### Opção 1: Automático com GitHub

1. **Fazer push do código para GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Conectar ao Vercel**
   - Acesse https://vercel.com
   - Clique em "New Project"
   - Selecione seu repositório GitHub
   - Vercel detectará automaticamente `vercel.json`
   - Clique em "Deploy"

### Opção 2: Manual com Vercel CLI

```bash
# Instalar Vercel CLI
npm install -g vercel

# Fazer deploy
vercel

# Para produção
vercel --prod
```

### Configuração Vercel

O arquivo `vercel.json` já está configurado com:
- Build command: `pip install -r requirements.txt && pelican content -o output -s pelicanconf.py`
- Output directory: `output`

## 🔧 Comandos Úteis

```bash
# Gerar site com recarregamento automático
pelican -l -r content -o output -s pelicanconf.py

# Gerar site uma vez
pelican content -o output -s pelicanconf.py

# Limpar arquivos gerados
pelican -l -r content -o output -s pelicanconf.py --delete-output-directory

# Instalar novos pacotes
pip install nome-do-pacote
pip freeze > requirements.txt
```

## 📊 Funcionalidades Incluídas

- [x] Homepage com posts recentes
- [x] Página de blog com todos os posts
- [x] Posts individuais com navegação
- [x] Página "Sobre"
- [x] Responsivo (mobile, tablet, desktop)
- [x] Feed RSS/Atom
- [x] Sitemap XML
- [x] Menu mobile (hambúrguer)
- [x] Dark mode support
- [x] Navegação entre posts

## 🎨 Personalizar o Design

### Adicionar imagens

1. Crie uma pasta `images` em `content/`
2. Coloque suas imagens lá
3. No Markdown, use: `![Descrição](/images/sua-imagem.jpg)`

### Adicionar CSS customizado

1. Crie `theme/static/css/custom.css`
2. Adicione em `theme/templates/base.html`:
   ```html
   <link rel="stylesheet" href="{{ SITEURL }}/theme/static/css/custom.css">
   ```

## 🐛 Solução de Problemas

### Posts não aparecem
- Verifique se o arquivo `.md` está em `content/`
- Confirme que os campos obrigatórios existem (Title, Date, Category, Tags, Slug)
- Certifique-se da data está no formato YYYY-MM-DD

### CSS não carrega
- Rode `pelican content -o output -s pelicanconf.py` novamente
- Limpe o cache do navegador (Ctrl+Shift+Delete)

### Erro ao fazer deploy
- Verifique se `vercel.json` existe
- Confira se `requirements.txt` está atualizado
- Veja os logs do Vercel para mais detalhes

## 📚 Recursos Adicionais

- [Documentação Pelican](https://docs.getpelican.com/)
- [Markdown Guide](https://www.markdownguide.org/)
- [Vercel Docs](https://vercel.com/docs)
- [Jinja2 Template Engine](https://jinja.palletsprojects.com/)

## 📄 Licença

Este projeto está disponível sob licença MIT. Sinta-se à vontade para usar, modificar e distribuir.

## ✨ Dicas Finais

1. **Consistência**: Publique regularmente para manter seus leitores engajados
2. **SEO**: Use slugs descritivos e tags relevantes
3. **Imagens**: Comprima imagens para melhor performance
4. **Backup**: Sempre mantenha cópias de seus posts
5. **Domínio**: Você pode conectar um domínio customizado no Vercel

---

**Criado com ❤️ para entusiastas de dados e Python**

Dúvidas? Sugestões? Abra uma issue ou entre em contato!
