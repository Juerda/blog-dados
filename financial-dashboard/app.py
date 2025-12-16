"""
Dashboard Financeiro Pessoal
Análise de extratos bancários OFX com categorização por LLM local
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import sys
import os

# Adicionar diretório raiz ao path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from utils.ofx_parser import OFXParser
from models.categorizer import TransactionCategorizer

# Configuração da página
st.set_page_config(
    page_title="Dashboard Financeiro Pessoal",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS customizado
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #0066CC;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
    .stButton>button {
        background-color: #0066CC;
        color: white;
        border-radius: 8px;
        padding: 0.5rem 2rem;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)


def init_session_state():
    """Inicializa estado da sessão"""
    if 'df' not in st.session_state:
        st.session_state.df = None
    if 'categorizer' not in st.session_state:
        st.session_state.categorizer = None
    if 'patterns_file' not in st.session_state:
        st.session_state.patterns_file = 'data/learned_patterns.json'


def load_ofx_file(uploaded_file):
    """Carrega e processa arquivo OFX"""
    parser = OFXParser()
    try:
        df = parser.parse_uploaded_file(uploaded_file)
        return df, None
    except Exception as e:
        return None, str(e)


def categorize_transactions(df, model_name):
    """Categoriza transações usando LLM"""
    try:
        categorizer = TransactionCategorizer(model_name=model_name)
        
        # Carregar padrões aprendidos anteriormente
        if os.path.exists(st.session_state.patterns_file):
            categorizer.load_learned_patterns(st.session_state.patterns_file)
        
        df = categorizer.categorize_batch(df)
        
        # Salvar novos padrões
        os.makedirs('data', exist_ok=True)
        categorizer.save_learned_patterns(st.session_state.patterns_file)
        
        st.session_state.categorizer = categorizer
        return df, None
    except Exception as e:
        return None, str(e)


def plot_category_pie(df):
    """Gráfico de pizza por categoria"""
    expenses = df[df['amount'] < 0].copy()
    expenses['amount'] = expenses['amount'].abs()
    
    category_sum = expenses.groupby('category')['amount'].sum().sort_values(ascending=False)
    
    fig = px.pie(
        values=category_sum.values,
        names=category_sum.index,
        title='Despesas por Categoria',
        hole=0.4,
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(height=500)
    
    return fig


def plot_monthly_trend(df):
    """Gráfico de tendência mensal"""
    df['month'] = df['date'].dt.to_period('M').astype(str)
    
    monthly = df.groupby('month').agg({
        'amount': lambda x: (x[x > 0].sum(), abs(x[x < 0].sum()))
    })
    
    monthly['income'] = monthly['amount'].apply(lambda x: x[0])
    monthly['expenses'] = monthly['amount'].apply(lambda x: x[1])
    monthly['balance'] = monthly['income'] - monthly['expenses']
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=monthly.index,
        y=monthly['income'],
        name='Receitas',
        marker_color='green'
    ))
    
    fig.add_trace(go.Bar(
        x=monthly.index,
        y=monthly['expenses'],
        name='Despesas',
        marker_color='red'
    ))
    
    fig.add_trace(go.Scatter(
        x=monthly.index,
        y=monthly['balance'],
        name='Saldo',
        mode='lines+markers',
        line=dict(color='blue', width=3)
    ))
    
    fig.update_layout(
        title='Análise Mensal',
        xaxis_title='Mês',
        yaxis_title='Valor (R$)',
        barmode='group',
        height=500
    )
    
    return fig


def plot_category_bars(df):
    """Gráfico de barras por categoria"""
    category_summary = df.groupby('category').agg({
        'amount': 'sum',
        'id': 'count'
    }).rename(columns={'id': 'count'})
    
    category_summary = category_summary.sort_values('amount')
    
    fig = px.bar(
        category_summary,
        y=category_summary.index,
        x='amount',
        orientation='h',
        title='Total por Categoria',
        labels={'amount': 'Valor (R$)', 'category': 'Categoria'},
        color='amount',
        color_continuous_scale='RdYlGn'
    )
    
    fig.update_layout(height=600)
    
    return fig


def main():
    """Função principal do dashboard"""
    init_session_state()
    
    # Header
    st.markdown('<h1 class="main-header">💰 Dashboard Financeiro Pessoal</h1>', unsafe_allow_html=True)
    st.markdown("**Análise inteligente de extratos bancários com LLM local**")
    st.markdown("---")
    
    # Sidebar
    with st.sidebar:
        st.header("⚙️ Configurações")
        
        # Modelo LLM
        model_name = st.selectbox(
            "Modelo LLM",
            ["llama3.2", "llama2", "mistral", "phi"],
            help="Modelo Ollama para categorização"
        )
        
        st.markdown("---")
        
        # Upload de arquivo
        st.header("📁 Upload de Extrato")
        uploaded_file = st.file_uploader(
            "Arquivo OFX",
            type=['ofx'],
            help="Faça upload do extrato bancário em formato OFX"
        )
        
        if uploaded_file:
            with st.spinner("Processando arquivo OFX..."):
                df, error = load_ofx_file(uploaded_file)
                
                if error:
                    st.error(f"❌ Erro ao processar: {error}")
                else:
                    st.success(f"✅ {len(df)} transações carregadas!")
                    
                    # Botão para categorizar
                    if st.button("🤖 Categorizar com LLM", type="primary"):
                        with st.spinner("Categorizando transações..."):
                            df_categorized, error = categorize_transactions(df, model_name)
                            
                            if error:
                                st.error(f"❌ Erro: {error}")
                            else:
                                st.session_state.df = df_categorized
                                st.success("✅ Categorização concluída!")
                                st.rerun()
        
        st.markdown("---")
        st.markdown("### 📊 Sobre")
        st.info("""
        Dashboard para análise de finanças pessoais com:
        - ✅ Leitura de extratos OFX
        - ✅ Categorização automática com LLM
        - ✅ Visualizações interativas
        - ✅ Aprendizado de padrões
        """)
    
    # Conteúdo principal
    if st.session_state.df is not None:
        df = st.session_state.df
        
        # Métricas resumo
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            total_income = df[df['amount'] > 0]['amount'].sum()
            st.metric("💰 Receitas", f"R$ {total_income:,.2f}")
        
        with col2:
            total_expenses = abs(df[df['amount'] < 0]['amount'].sum())
            st.metric("💸 Despesas", f"R$ {total_expenses:,.2f}")
        
        with col3:
            balance = total_income - total_expenses
            st.metric("💵 Saldo", f"R$ {balance:,.2f}", 
                     delta=f"{balance:,.2f}", 
                     delta_color="normal" if balance >= 0 else "inverse")
        
        with col4:
            st.metric("📝 Transações", len(df))
        
        st.markdown("---")
        
        # Abas
        tab1, tab2, tab3, tab4 = st.tabs(["📊 Visão Geral", "📋 Transações", "📈 Análises", "⚙️ Configurações"])
        
        with tab1:
            col1, col2 = st.columns(2)
            
            with col1:
                st.plotly_chart(plot_category_pie(df), use_container_width=True)
            
            with col2:
                st.plotly_chart(plot_category_bars(df), use_container_width=True)
            
            st.plotly_chart(plot_monthly_trend(df), use_container_width=True)
        
        with tab2:
            st.header("📋 Lista de Transações")
            
            # Filtros
            col1, col2, col3 = st.columns(3)
            
            with col1:
                categories = ['Todas'] + sorted(df['category'].unique().tolist())
                selected_category = st.selectbox("Categoria", categories)
            
            with col2:
                transaction_types = ['Todas', 'Receitas', 'Despesas']
                selected_type = st.selectbox("Tipo", transaction_types)
            
            with col3:
                date_range = st.date_input(
                    "Período",
                    value=(df['date'].min(), df['date'].max())
                )
            
            # Aplicar filtros
            df_filtered = df.copy()
            
            if selected_category != 'Todas':
                df_filtered = df_filtered[df_filtered['category'] == selected_category]
            
            if selected_type == 'Receitas':
                df_filtered = df_filtered[df_filtered['amount'] > 0]
            elif selected_type == 'Despesas':
                df_filtered = df_filtered[df_filtered['amount'] < 0]
            
            if len(date_range) == 2:
                df_filtered = df_filtered[
                    (df_filtered['date'].dt.date >= date_range[0]) & 
                    (df_filtered['date'].dt.date <= date_range[1])
                ]
            
            # Exibir tabela
            st.dataframe(
                df_filtered[['date', 'description', 'category', 'amount']].style.format({
                    'date': lambda x: x.strftime('%d/%m/%Y'),
                    'amount': 'R$ {:.2f}'
                }),
                use_container_width=True,
                height=500
            )
            
            # Download CSV
            csv = df_filtered.to_csv(index=False).encode('utf-8')
            st.download_button(
                "📥 Download CSV",
                csv,
                "transacoes.csv",
                "text/csv"
            )
        
        with tab3:
            st.header("📈 Análises Detalhadas")
            
            # Resumo por categoria
            st.subheader("Por Categoria")
            if st.session_state.categorizer:
                summary = st.session_state.categorizer.get_category_summary(df)
                st.dataframe(summary.style.format({
                    'Total': 'R$ {:.2f}',
                    'Média': 'R$ {:.2f}'
                }), use_container_width=True)
            
            # Top 10 maiores despesas
            st.subheader("🔴 Top 10 Maiores Despesas")
            top_expenses = df[df['amount'] < 0].nlargest(10, 'amount', keep='first')
            top_expenses['amount'] = top_expenses['amount'].abs()
            
            fig = px.bar(
                top_expenses,
                x='amount',
                y='description',
                orientation='h',
                title='Maiores Despesas',
                labels={'amount': 'Valor (R$)', 'description': 'Descrição'},
                color='category',
                color_discrete_sequence=px.colors.qualitative.Set2
            )
            st.plotly_chart(fig, use_container_width=True)
            
            # Top 10 maiores receitas
            st.subheader("🟢 Top 10 Maiores Receitas")
            top_income = df[df['amount'] > 0].nlargest(10, 'amount', keep='first')
            
            fig = px.bar(
                top_income,
                x='amount',
                y='description',
                orientation='h',
                title='Maiores Receitas',
                labels={'amount': 'Valor (R$)', 'description': 'Descrição'},
                color='category',
                color_discrete_sequence=px.colors.qualitative.Set1
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with tab4:
            st.header("⚙️ Configurações Avançadas")
            
            st.subheader("🧠 Padrões Aprendidos")
            if st.session_state.categorizer and st.session_state.categorizer.learned_patterns:
                patterns_df = pd.DataFrame([
                    {'Descrição': k, 'Categoria': v} 
                    for k, v in st.session_state.categorizer.learned_patterns.items()
                ])
                st.dataframe(patterns_df, use_container_width=True)
                
                if st.button("🗑️ Limpar Padrões Aprendidos"):
                    if os.path.exists(st.session_state.patterns_file):
                        os.remove(st.session_state.patterns_file)
                    st.session_state.categorizer.learned_patterns = {}
                    st.success("Padrões limpos!")
                    st.rerun()
            else:
                st.info("Nenhum padrão aprendido ainda.")
            
            st.markdown("---")
            
            st.subheader("📊 Exportar Dados")
            
            # Exportar completo
            full_csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                "📥 Exportar Todas as Transações (CSV)",
                full_csv,
                "transacoes_completas.csv",
                "text/csv"
            )
            
            # Exportar resumo
            if st.session_state.categorizer:
                summary = st.session_state.categorizer.get_category_summary(df)
                summary_csv = summary.to_csv().encode('utf-8')
                st.download_button(
                    "📥 Exportar Resumo por Categoria (CSV)",
                    summary_csv,
                    "resumo_categorias.csv",
                    "text/csv"
                )
    
    else:
        # Tela inicial
        st.info("👈 Faça upload de um arquivo OFX na barra lateral para começar!")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            ### 📁 Passo 1
            Faça upload do seu extrato bancário em formato **OFX** na barra lateral.
            """)
        
        with col2:
            st.markdown("""
            ### 🤖 Passo 2
            Clique em **Categorizar com LLM** para que a IA analise e categorize suas transações.
            """)
        
        with col3:
            st.markdown("""
            ### 📊 Passo 3
            Explore as visualizações, análises e exporte os dados conforme necessário.
            """)
        
        st.markdown("---")
        
        st.markdown("""
        ### 💡 Recursos Disponíveis
        
        - **✅ Leitura automática de OFX**: Suporta extratos de diversos bancos brasileiros
        - **✅ Categorização inteligente**: LLM local analisa e categoriza cada transação
        - **✅ Aprendizado de padrões**: Sistema aprende com suas transações
        - **✅ Visualizações interativas**: Gráficos de pizza, barras e tendências
        - **✅ Análises detalhadas**: Top despesas, receitas, resumos por categoria
        - **✅ Filtros avançados**: Por categoria, tipo, período
        - **✅ Export em CSV**: Baixe seus dados para análises externas
        - **✅ Privacidade total**: Tudo roda localmente, seus dados não saem do seu computador
        """)


if __name__ == "__main__":
    main()
