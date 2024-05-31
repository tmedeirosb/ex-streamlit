import streamlit as st
from pycaret.datasets import get_data
import seaborn as sns
import matplotlib.pyplot as plt
import time
import pandas as pd
import plotly.express as px


st.set_page_config(page_title='Testes Streamlit', page_icon=':rocket:')

st.write("<h1> Testes diversos com Streamlit </h1>", unsafe_allow_html=True)

# Carregar dados de exemplo para obter nomes de características
data = get_data('cancer')
st.session_state.data = data

st.download_button('Baixar dados', st.session_state.data.to_csv(index=False), 'cancer.csv', 'csv')

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


st.subheader('Teste expander')

with st.expander('Veja mais'):
    st.write('Texto expandido')

st.subheader('Teste de formulário')

with st.form(key='form'):
    nome = st.text_input('Nome')
    idade = st.number_input('Idade', min_value=0, max_value=100)
    sexo = st.radio('Sexo', ['Masculino', 'Feminino'])
    cor = st.selectbox('Cor', ['Branco', 'Preto', 'Pardo'])
    enviar = st.form_submit_button('Enviar')
    nascimento = st.date_input('Data de nascimento', min_value=pd.to_datetime('1900-01-01'), max_value=pd.to_datetime('2022-01-01'))

if enviar:  
    st.write(f'Nome: {nome}, Idade: {idade}, Sexo: {sexo}, Cor: {cor}, Data de nascimento: {nascimento}')


st.subheader('Teste de plotly')

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv")
st.dataframe(df)

fig = px.scatter(df.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent")
st.plotly_chart(fig)

df_continent = df.groupby(['continent', 'year'])['gdpPercap'].mean().reset_index()
fig = px.line(df_continent, x="year", y="gdpPercap", color="continent")
st.plotly_chart(fig)

fig = px.bar(df, x='year', y='pop', color='continent')
st.plotly_chart(fig)