# 📖 Como Fazer Upload do Blog para GitHub

## Passo 1: Criar um Repositório no GitHub

1. Acesse https://github.com/new
2. Faça login com sua conta (neste caso: **Juerda**)
3. Preencha os dados:
   - **Repository name**: `blog-dados` (ou o nome que preferir)
   - **Description**: "Blog de análises de dados com Python e Pelican"
   - **Public**: Marque se quiser que todos vejam (recomendado para portfólio)
   - **Add .gitignore**: Não adicione (já temos o .gitignore)
   - **Add README.md**: Não adicione (já temos)

4. Clique em **Create repository**

## Passo 2: Conectar o Repositório Local ao GitHub

Após criar o repositório, copie o URL do repositório (algo como `https://github.com/Juerda/blog-dados.git` ou `git@github.com:Juerda/blog-dados.git`)

Depois execute no terminal (dentro da pasta do projeto):

```bash
# Adicionar o repositório remoto
git remote add origin https://github.com/Juerda/blog-dados.git

# Renomear a branch de 'master' para 'main' (opcional, mas recomendado)
git branch -M main

# Fazer o push inicial (enviar arquivos para GitHub)
git push -u origin main
```

## Passo 3: Verificar no GitHub

1. Acesse seu repositório em `https://github.com/Juerda/blog-dados`
2. Você verá todos os arquivos do projeto lá!

## Passo 4: Deploy no Vercel (Automático)

Agora que seu código está no GitHub, você pode fazer deploy automático:

1. Acesse https://vercel.com
2. Clique em "Import Project"
3. Selecione "Import Git Repository"
4. Procure por `blog-dados` (seu repositório)
5. Clique em "Import"
6. Vercel detectará automaticamente o `vercel.json`
7. Clique em "Deploy"

**Pronto! Seu blog estará online em um domínio do Vercel!**

## 📝 Depois de Fazer Upload

Sempre que quiser fazer mudanças:

```bash
# Fazer alterações nos arquivos

# Adicionar as mudanças
git add .

# Fazer commit com uma mensagem
git commit -m "Descrição das mudanças"

# Fazer push para GitHub
git push
```

Vercel detectará automaticamente as mudanças e fará o redeploy! 🚀

---

**Seu repositório estará visível em**: `https://github.com/Juerda/blog-dados`

**Seu blog estará online em**: `https://seu-dominio.vercel.app`

