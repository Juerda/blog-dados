# 📚 COMO FAZER UPLOAD PARA GITHUB - PASSO A PASSO

## Seu Git já está pronto! ✅

Seu projeto já está versionado localmente. Agora precisa ser enviado para o GitHub.

## PASSO 1: Criar repositório no GitHub
**Tempo: 2 minutos**

```
1. Acesse https://github.com/new
2. Faça login com: Juerda
3. Preencha:
   - Repository name: blog-dados
   - Description: Blog de análises de dados
   - Deixe como Public (para portfólio)
4. Clique em "Create repository"
5. COPIE o URL que aparece (vai ser algo como):
   https://github.com/Juerda/blog-dados.git
```

## PASSO 2: Conectar seu projeto local ao GitHub
**Tempo: 1 minuto**

Abra o PowerShell dentro da pasta `Projeto - Blog` e execute:

```powershell
# Cole exatamente o que apareceu na tela do GitHub:
git remote add origin https://github.com/Juerda/blog-dados.git

# Mude a branch para "main":
git branch -M main

# Envie seus arquivos:
git push -u origin main
```

**Isso é tudo!** ✨

## Pronto! Verifique:

Acesse: https://github.com/Juerda/blog-dados

Você verá todos seus arquivos lá! 📁

---

## Próximo: Deploy no Vercel (Automático)

Depois que estiver no GitHub:

```
1. Acesse https://vercel.com
2. Clique em "Add New" → "Project"
3. Selecione "blog-dados"
4. Clique em "Deploy"
```

**Seu blog estará online!** 🚀

---

## 📝 Atualizações Futuras

Sempre que quiser atualizar seu blog:

```powershell
# Opção 1: Manualmente
git add .
git commit -m "Adicionado novo post"
git push

# Opção 2: Usar o script
.\push.bat "Adicionado novo post"
```

---

## 🔍 Comandos Úteis

```powershell
# Ver status
git status

# Ver commits feitos
git log --oneline

# Ver branches
git branch -a
```

---

**💡 Dúvidas? Consulte os arquivos:**
- `README.md` - Documentação completa
- `GITHUB_SETUP.md` - Instruções detalhadas
- `INSTRUÇÕES_GITHUB.md` - Referência técnica

**Sucesso! 🎉**
