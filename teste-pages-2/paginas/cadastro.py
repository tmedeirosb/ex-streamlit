import streamlit as st
import pandas as pd

st.title('Página Cadastro')

def frm_cadastro():
    st.write('Cadastro de usuário')
    with st.form(key='cadastro_form'):
        nome = st.text_input('Nome')
        email = st.text_input('Email')
        senha = st.text_input('Senha', type='password')
        submit_button = st.form_submit_button(label='Cadastrar')

    if submit_button:
        try:
            df = pd.read_csv('data/usuarios.csv')
        except:
            df = pd.DataFrame(columns=['nome', 'email', 'senha'])
        
        df = pd.concat([df, pd.DataFrame({'nome': [nome], 'email': [email], 'senha': [senha]})])
        df.to_csv('data/usuarios.csv', index=False)
        st.success('Usuário cadastrado com sucesso')