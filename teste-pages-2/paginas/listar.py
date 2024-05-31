import streamlit as st
import pandas as pd

st.title('Listar usuário')

def df_listar():
    try:
        df = pd.read_csv('data/usuarios.csv')
        st.dataframe(df)
    except:
        st.write('Nenhum usuário cadastrado')
    
    