"""
Parser de arquivos OFX (Open Financial Exchange)
Lê extratos bancários e retorna DataFrame com transações
"""

import ofxparse
import pandas as pd
from datetime import datetime
from typing import List, Dict, Any
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class OFXParser:
    """Classe para processar arquivos OFX de extratos bancários"""
    
    def __init__(self):
        self.transactions = []
    
    def parse_file(self, file_path: str) -> pd.DataFrame:
        """
        Lê arquivo OFX e retorna DataFrame com transações
        
        Args:
            file_path: Caminho para arquivo OFX
            
        Returns:
            DataFrame com colunas: date, description, amount, type, balance
        """
        try:
            with open(file_path, 'rb') as file:
                ofx = ofxparse.OfxParser.parse(file)
            
            transactions = []
            
            # Processar cada conta no arquivo
            for account in ofx.accounts:
                logger.info(f"Processando conta: {account.account_id}")
                
                # Extrair transações
                for transaction in account.statement.transactions:
                    transactions.append({
                        'date': transaction.date,
                        'description': transaction.payee or transaction.memo or 'Sem descrição',
                        'amount': float(transaction.amount),
                        'type': transaction.type,
                        'id': transaction.id,
                        'category': None,  # Será preenchido pelo LLM
                        'account_id': account.account_id
                    })
            
            df = pd.DataFrame(transactions)
            
            if not df.empty:
                df['date'] = pd.to_datetime(df['date'])
                df = df.sort_values('date', ascending=False)
                logger.info(f"Total de transações processadas: {len(df)}")
            else:
                logger.warning("Nenhuma transação encontrada no arquivo")
            
            return df
            
        except Exception as e:
            logger.error(f"Erro ao processar arquivo OFX: {str(e)}")
            raise
    
    def parse_uploaded_file(self, uploaded_file) -> pd.DataFrame:
        """
        Lê arquivo OFX do upload do Streamlit
        
        Args:
            uploaded_file: Objeto UploadedFile do Streamlit
            
        Returns:
            DataFrame com transações
        """
        try:
            ofx = ofxparse.OfxParser.parse(uploaded_file)
            
            transactions = []
            
            for account in ofx.accounts:
                for transaction in account.statement.transactions:
                    transactions.append({
                        'date': transaction.date,
                        'description': transaction.payee or transaction.memo or 'Sem descrição',
                        'amount': float(transaction.amount),
                        'type': transaction.type,
                        'id': transaction.id,
                        'category': None,
                        'account_id': account.account_id
                    })
            
            df = pd.DataFrame(transactions)
            
            if not df.empty:
                df['date'] = pd.to_datetime(df['date'])
                df = df.sort_values('date', ascending=False)
            
            return df
            
        except Exception as e:
            logger.error(f"Erro ao processar upload: {str(e)}")
            raise
    
    @staticmethod
    def get_summary(df: pd.DataFrame) -> Dict[str, Any]:
        """
        Gera resumo estatístico das transações
        
        Args:
            df: DataFrame com transações
            
        Returns:
            Dicionário com estatísticas
        """
        if df.empty:
            return {}
        
        return {
            'total_transactions': len(df),
            'total_income': df[df['amount'] > 0]['amount'].sum(),
            'total_expenses': abs(df[df['amount'] < 0]['amount'].sum()),
            'net_balance': df['amount'].sum(),
            'date_range': {
                'start': df['date'].min(),
                'end': df['date'].max()
            },
            'avg_transaction': df['amount'].mean(),
            'largest_expense': df[df['amount'] < 0]['amount'].min(),
            'largest_income': df[df['amount'] > 0]['amount'].max()
        }
