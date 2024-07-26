#pip install streamlit pandas pandas-profiling streamlit-pandas-profiling


import streamlit as st
import pandas as pd
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

st.title('Pandas Profiling DataFrame')

# Carrega o DataFrame a partir de um arquivo CSV
df = pd.read_csv("https://storage.googleapis.com/tf-datasets/titanic/train.csv")

# Gera o relatório de perfil do DataFrame
pr = ProfileReport(df, explorative=True)

# Exibe o relatório no Streamlit
st_profile_report(pr)
