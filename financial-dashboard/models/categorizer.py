"""
Categorizador de transações usando LLM local (Ollama)
"""

import ollama
import pandas as pd
from typing import List, Dict, Optional
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TransactionCategorizer:
    """Categoriza transações financeiras usando LLM local"""
    
    # Categorias padrão brasileiras
    CATEGORIES = {
        'Alimentação': ['supermercado', 'restaurante', 'lanchonete', 'padaria', 'açougue', 
                        'mercado', 'ifood', 'uber eats', 'rappi'],
        'Transporte': ['uber', '99', 'combustível', 'gasolina', 'estacionamento', 
                       'metrô', 'ônibus', 'taxi', 'pedágio'],
        'Moradia': ['aluguel', 'condomínio', 'iptu', 'água', 'luz', 'energia', 
                    'gás', 'internet', 'telefone'],
        'Saúde': ['farmácia', 'médico', 'hospital', 'plano de saúde', 'dentista', 
                  'exame', 'laboratório'],
        'Educação': ['escola', 'faculdade', 'curso', 'livro', 'material escolar'],
        'Lazer': ['cinema', 'streaming', 'netflix', 'spotify', 'academia', 'viagem', 
                  'hotel', 'ingresso'],
        'Vestuário': ['roupa', 'calçado', 'loja', 'shopping'],
        'Serviços': ['cabeleireiro', 'barbeiro', 'lavanderia', 'conserto'],
        'Investimentos': ['aplicação', 'poupança', 'cdb', 'tesouro', 'ações', 'corretora'],
        'Receitas': ['salário', 'freelance', 'venda', 'reembolso', 'rendimento'],
        'Transferências': ['pix', 'ted', 'doc', 'transferência'],
        'Outros': []
    }
    
    def __init__(self, model_name: str = "llama3.2"):
        """
        Inicializa categorizador
        
        Args:
            model_name: Nome do modelo Ollama (padrão: llama3.2)
        """
        self.model_name = model_name
        self.learned_patterns = {}
        self._check_ollama()
    
    def _check_ollama(self):
        """Verifica se Ollama está disponível"""
        try:
            models = ollama.list()
            logger.info(f"Ollama disponível. Modelos: {[m['name'] for m in models['models']]}")
        except Exception as e:
            logger.error(f"Ollama não está disponível: {str(e)}")
            raise ConnectionError(
                "Ollama não está rodando. Execute: 'ollama serve' em outro terminal"
            )
    
    def categorize_transaction(self, description: str, amount: float) -> str:
        """
        Categoriza uma transação usando LLM
        
        Args:
            description: Descrição da transação
            amount: Valor (positivo = receita, negativo = despesa)
            
        Returns:
            Categoria identificada
        """
        # Verificar cache de padrões aprendidos
        desc_lower = description.lower()
        for pattern, category in self.learned_patterns.items():
            if pattern in desc_lower:
                logger.info(f"Categoria encontrada no cache: {category}")
                return category
        
        # Usar LLM para categorizar
        prompt = self._build_prompt(description, amount)
        
        try:
            response = ollama.chat(
                model=self.model_name,
                messages=[{
                    'role': 'user',
                    'content': prompt
                }]
            )
            
            category = response['message']['content'].strip()
            
            # Validar categoria
            if category in self.CATEGORIES:
                # Aprender padrão para próximas vezes
                self.learned_patterns[desc_lower] = category
                return category
            else:
                # Tentar encontrar categoria mais próxima
                for cat in self.CATEGORIES.keys():
                    if cat.lower() in category.lower():
                        self.learned_patterns[desc_lower] = cat
                        return cat
                
                return 'Outros'
            
        except Exception as e:
            logger.error(f"Erro ao categorizar com LLM: {str(e)}")
            return self._fallback_categorization(description, amount)
    
    def _build_prompt(self, description: str, amount: float) -> str:
        """Constrói prompt para o LLM"""
        transaction_type = "RECEITA" if amount > 0 else "DESPESA"
        
        categories_list = '\n'.join([f"- {cat}" for cat in self.CATEGORIES.keys()])
        
        prompt = f"""Você é um assistente financeiro especializado em categorizar transações bancárias brasileiras.

TRANSAÇÃO:
Descrição: {description}
Valor: R$ {amount:.2f}
Tipo: {transaction_type}

CATEGORIAS DISPONÍVEIS:
{categories_list}

INSTRUÇÕES:
1. Analise a descrição da transação
2. Identifique a categoria mais apropriada
3. Responda APENAS com o nome exato da categoria (sem explicações)
4. Se não tiver certeza, escolha "Outros"

CATEGORIA:"""
        
        return prompt
    
    def _fallback_categorization(self, description: str, amount: float) -> str:
        """Categorização por palavras-chave (fallback se LLM falhar)"""
        desc_lower = description.lower()
        
        # Receitas
        if amount > 0:
            return 'Receitas'
        
        # Buscar por palavras-chave
        for category, keywords in self.CATEGORIES.items():
            for keyword in keywords:
                if keyword in desc_lower:
                    return category
        
        return 'Outros'
    
    def categorize_batch(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Categoriza todas as transações de um DataFrame
        
        Args:
            df: DataFrame com colunas 'description' e 'amount'
            
        Returns:
            DataFrame com coluna 'category' preenchida
        """
        logger.info(f"Categorizando {len(df)} transações...")
        
        df['category'] = df.apply(
            lambda row: self.categorize_transaction(
                row['description'], 
                row['amount']
            ),
            axis=1
        )
        
        logger.info("Categorização concluída!")
        return df
    
    def get_category_summary(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Gera resumo por categoria
        
        Args:
            df: DataFrame categorizado
            
        Returns:
            DataFrame com resumo por categoria
        """
        summary = df.groupby('category').agg({
            'amount': ['sum', 'count', 'mean']
        }).round(2)
        
        summary.columns = ['Total', 'Quantidade', 'Média']
        summary = summary.sort_values('Total')
        
        return summary
    
    def save_learned_patterns(self, file_path: str):
        """Salva padrões aprendidos em arquivo JSON"""
        import json
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(self.learned_patterns, f, ensure_ascii=False, indent=2)
        logger.info(f"Padrões salvos em {file_path}")
    
    def load_learned_patterns(self, file_path: str):
        """Carrega padrões aprendidos de arquivo JSON"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                self.learned_patterns = json.load(f)
            logger.info(f"{len(self.learned_patterns)} padrões carregados")
        except FileNotFoundError:
            logger.info("Nenhum arquivo de padrões encontrado")
