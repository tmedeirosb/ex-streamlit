import streamlit as st
from pycaret.datasets import get_data
import seaborn as sns
import matplotlib.pyplot as plt
import time
import pandas as pd


st.set_page_config(page_title='Testes Streamlit', page_icon=':rocket:')

st.write("<h1> Testes diversos com Streamlit </h1>", unsafe_allow_html=True)

# Carregar dados de exemplo para obter nomes de características
data = get_data('cancer')

st.write('Teste st.dataframe')
st.dataframe(data)

#st.write('Teste st.table')
#st.table(data)

st.write('Teste st.write')
st.write(data)

st.markdown('---')
st.subheader('Teste midias')

st.image('docs/eu.png', width=100)
st.video('docs/IMG_7746.mov')


# st.subheader('Teste de file uploader')
# diario = st.file_uploader('Escolha um arquivo CSV', type='csv')
# if diario:
#     st.dataframe(diario)

st.subheader('Teste de gráficos')

bt = st.button('Gerar gráficos')
if bt:
    plt.figure()  # Cria uma nova figura
    sns.scatterplot(data=data, x='menopause', y='tumor-size', hue='Class')
    st.pyplot(plt.gcf())


st.subheader('Teste de barra de progresso')

# st.empty()
# progresso = st.progress(0)

# for i in range(100):
#     progresso.progress(i+1)
#     time.sleep(0.1)

def carregar_dados(file):
    df = pd.read_csv(file)
    n_linhas, n_colunas = df.shape
    st.write(f'Número de linhas: {n_linhas} e número de colunas: {n_colunas}')
    return df

file = st.file_uploader('Escolha um arquivo CSV', type='csv')
if file:
    with st.spinner('Carregando dados...'):
        df = carregar_dados(file)
    st.success('Dados carregados com sucesso!')
    st.dataframe(df)