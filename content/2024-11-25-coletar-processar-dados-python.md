Title: Como Coletar e Processar Dados com Python
Date: 2024-11-25
Category: Python
Tags: python, dados, programação
Slug: coletar-processar-dados-python

## Introdução

Neste post, vou mostrar técnicas práticas para coletar e processar dados usando Python, uma das linguagens mais populares para ciência de dados.

## Coleta de Dados

Existem várias formas de coletar dados:

### 1. APIs
```python
import requests

response = requests.get('https://api.example.com/data')
data = response.json()
```

### 2. Web Scraping
```python
from bs4 import BeautifulSoup

html = requests.get('https://example.com').text
soup = BeautifulSoup(html, 'html.parser')
```

### 3. Arquivos Locais
```python
import pandas as pd

df = pd.read_csv('dados.csv')
```

## Processamento de Dados

Após coletar os dados, é importante processá-los adequadamente:

- **Limpeza**: Remover valores nulos e duplicatas
- **Transformação**: Converter tipos de dados
- **Normalização**: Padronizar valores
- **Enriquecimento**: Adicionar dados complementares

## Exemplo Prático

```python
import pandas as pd
import numpy as np

# Carregar dados
df = pd.read_csv('vendas.csv')

# Limpeza
df = df.dropna()
df = df.drop_duplicates()

# Análise
media_vendas = df['valor'].mean()
```

## Conclusão

Python oferece um ecossistema robusto para trabalhar com dados. As bibliotecas como Pandas, NumPy e Requests tornam a coleta e processamento muito mais acessível.

