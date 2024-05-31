import streamlit as st
import pandas as pd
import plotly.express as px
from bokeh.plotting import figure
import altair as alt

@st.cache_data()
def read_df(path):
    return pd.read_csv(path)

st.title("SF Tree - Marilia")
st.subheader("Plotly chart")

trees_df = read_df("data/trees.csv")

#plotly
fig = px.histogram(trees_df['dbh'])
st.plotly_chart(fig)

#bokeh
scatterplot = figure(title="Scatterplot")
scatterplot.scatter(trees_df['dbh'], trees_df['site_order'])
scatterplot.xaxis.axis_label = "DBH"
st.bokeh_chart(scatterplot)

#altair
df_caretaker = trees_df.groupby(['caretaker']).count()['tree_id'].reset_index()
df_caretaker.columns = ['caretaker', 'tree_count']

fig = alt.Chart(df_caretaker).mark_bar().encode(x = 'caretaker', y = 'tree_count')
st.altair_chart(fig)

fig = alt.Chart(trees_df).mark_bar().encode(x = 'caretaker', y = 'count(*):Q')
st.altair_chart(fig)