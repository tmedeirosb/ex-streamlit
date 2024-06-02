import streamlit as st
import os

def is_running_on_streamlit_cloud():
    # Verificar a variável de ambiente específica do Streamlit Cloud
    #return "STREAMLIT_SERVER_EMAIL" in os.environ
    return "HOSTNAME" in os.environ

#st.write("Variáveis de ambiente disponíveis:", os.environ)

if is_running_on_streamlit_cloud():
    st.write("A aplicação está rodando na nuvem (Streamlit Cloud).")
    
    # Acessar a chave da API
    key_secret = os.getenv("KEY_SECRET")
    key_user = st.text_input("Digite a chave de acesso", type="password")
    if key_user == key_secret:
        st.write("Acesso liberado!")
    else:
        st.write("Acesso negado!")
        st.stop()
        
else:
    st.write("A aplicação está rodando localmente.")