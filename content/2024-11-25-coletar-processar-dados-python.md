Title: Como Coletar e Processar Dados com Python
Date: 2024-11-25
Category: Python
Tags: python, dados, programação
Slug: coletar-processar-dados-python

## Introdução

Neste post, vou mostrar técnicas práticas para coletar e processar dados usando Python, uma das linguagens mais populares para ciência de dados.

## Principais Métodos de Coleta de Dados

<div class="pie-chart-container">
  <h3 style="text-align: center; margin-top: 0;">Métodos Mais Utilizados para Coleta</h3>
  
  <button class="csv-export-button" data-target="methodsPieChart" data-filename="metodos-coleta-dados.csv" data-title="Métodos de Coleta de Dados - Python">
    📥 Baixar Dados em CSV
  </button>
  
  <div class="pie-chart-wrapper">
    <div class="pie-chart-canvas">
      <canvas id="methodsPieChart" width="300" height="300"></canvas>
    </div>
    
    <div class="pie-chart-legend">
      <div class="pie-chart-legend-item">
        <div class="pie-chart-legend-color" style="background: #3498db;"></div>
        <span><strong>APIs REST:</strong> 40%</span>
      </div>
      <div class="pie-chart-legend-item">
        <div class="pie-chart-legend-color" style="background: #e74c3c;"></div>
        <span><strong>Web Scraping:</strong> 25%</span>
      </div>
      <div class="pie-chart-legend-item">
        <div class="pie-chart-legend-color" style="background: #f39c12;"></div>
        <span><strong>Arquivos CSV:</strong> 20%</span>
      </div>
      <div class="pie-chart-legend-item">
        <div class="pie-chart-legend-color" style="background: #2ecc71;"></div>
        <span><strong>Banco de Dados:</strong> 10%</span>
      </div>
      <div class="pie-chart-legend-item">
        <div class="pie-chart-legend-color" style="background: #9b59b6;"></div>
        <span><strong>Outros:</strong> 5%</span>
      </div>
    </div>
  </div>
</div>

<script>
  // Dados para o gráfico de pizza
  const methodsData = [
    { label: 'APIs REST', value: 40, percentage: 40 },
    { label: 'Web Scraping', value: 25, percentage: 25 },
    { label: 'Arquivos CSV', value: 20, percentage: 20 },
    { label: 'Banco de Dados', value: 10, percentage: 10 },
    { label: 'Outros', value: 5, percentage: 5 }
  ];

  const methodsColors = ['#3498db', '#e74c3c', '#f39c12', '#2ecc71', '#9b59b6'];

  // Inicializar gráfico de pizza
  const methodsPieChart = new PieChart('methodsPieChart', methodsData, methodsColors);
  
  // Armazenar os dados para exportação CSV
  window.pieCharts = window.pieCharts || {};
  window.pieCharts.methodsPieChart = {
    getData: function() {
      return [
        { Método: 'APIs REST', Percentual: '40%', Preferência: 'Muito Alta' },
        { Método: 'Web Scraping', Percentual: '25%', Preferência: 'Alta' },
        { Método: 'Arquivos CSV', Percentual: '20%', Preferência: 'Alta' },
        { Método: 'Banco de Dados', Percentual: '10%', Preferência: 'Média' },
        { Método: 'Outros', Percentual: '5%', Preferência: 'Baixa' }
      ];
    }
  };
</script>

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

