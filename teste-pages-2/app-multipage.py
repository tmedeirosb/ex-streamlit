import streamlit as st

from paginas import cadastro, listar

st.title('Página inicial')

st.sidebar.markdown('## Menu')
pagina = st.sidebar.selectbox('Selecione', options=['Cadastro', 'Listar'])

if pagina == 'Cadastro':
    cadastro.frm_cadastro()
elif pagina == 'Listar':
    listar.df_listar()