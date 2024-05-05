import streamlit as st
from pycaret.datasets import get_data

# Carregar dados de exemplo para obter nomes de características
data = get_data('cancer')

st.write('Teste st.dataframe')
st.dataframe(data)

#st.write('Teste st.table')
#st.table(data)

st.write('Teste st.write')
st.write(data)



