import streamlit as st
import pandas as pd
import plotly.express as px
from bokeh.plotting import figure
import altair as alt

st.set_page_config(layout='wide')

@st.cache_data()
def read_df(path):
    return pd.read_csv(path)

st.title("SF Tree")
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

graph_color = st.sidebar.color_picker("Graph Colors")

#col1, col2, col3 = st.columns(3)
col1, col2, col3 = st.columns(3, gap="large")

with col1:
     st.line_chart(df_caretaker)
with col2:
     st.bar_chart(df_caretaker)
with col3:
     st.area_chart(df_caretaker)

tab1, tab2, tab3 = st.tabs(["Line Chart", "Bar Chart", "Area Chart"])
with tab1:
    #st.line_chart(df_caretaker)
    fig = px.histogram(
        trees_df,
        x=trees_df["dbh"],
        title="Tree Age",
        color_discrete_sequence=[graph_color])
    st.plotly_chart(fig, use_container_width=True)
with tab2:
    st.bar_chart(df_caretaker)
with tab3:
    st.area_chart(df_caretaker)