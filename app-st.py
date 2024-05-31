import streamlit as st
from pycaret.datasets import get_data
from pycaret.classification import load_model, predict_model
import numpy as np
import pandas as pd
import os


def is_running_on_streamlit_cloud():
    # Verificar a variável de ambiente específica do Streamlit Cloud
    #return "STREAMLIT_SERVER_EMAIL" in os.environ
    return "HOSTNAME" in os.environ

#st.write("Variáveis de ambiente disponíveis:", os.environ)

if is_running_on_streamlit_cloud():
    st.write("A aplicação está rodando na nuvem (Streamlit Cloud).")
    
    # Acessar a chave da API
    #api_key = os.getenv("KEY_SECRET")
else:
    st.write("A aplicação está rodando localmente.")

#import pycaret
#st.write(pycaret.__version__)

# Carregar o modelo treinado
model = load_model('final_cancer')

# Carregar dados de exemplo para obter nomes de características
data = get_data('cancer')
data = data.drop(['Class'], axis=1)  # Remover a coluna de saída para obter apenas características

# Título da Aplicação
st.title('Predição de Câncer com PyCaret e Streamlit - SECRECT KEY')

# Criar filtros para cada característica
inputs = {}
for col in data.columns:
    # Identificar o tipo da coluna para decidir o tipo de filtro (slider para numéricos)
    if np.issubdtype(data[col].dtype, np.number):
        min_val = float(data[col].min())
        max_val = float(data[col].max())
        default_val = float(data[col].median())
        inputs[col] = st.slider(label=col, min_value=min_val, max_value=max_val, value=default_val)
    else:
        # Se não for numérico, considerar como categórico (opção seletiva)
        options = list(data[col].unique())
        default_val = options[0]
        inputs[col] = st.selectbox(label=col, options=options, index=0)

# Botão para fazer a previsão
if st.button('Prever'):
    # Transformar os dados de entrada em DataFrame
    input_df = pd.DataFrame([inputs])
    
    # Fazer a previsão
    prediction = predict_model(model, data=input_df)
    #prediction_label = prediction['Label'][0]
    
    # Exibir a previsão
    #st.write(f'O resultado previsto é: {prediction}')
    st.write( f'O resultado previsto é: {prediction["prediction_score"][0]}' )