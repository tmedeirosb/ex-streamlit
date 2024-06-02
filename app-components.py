# pip install ...
# streamlit-aggrid 
# streamlit-plotly-events
# streamlit-lottie 
# streamlit-pandas-profiling
# streamlit-folium
# streamlit-extras

import streamlit as st
import pandas as pd

#AGGRID
from st_aggrid import AgGrid

trees_df = pd.read_csv("data/trees.csv")
trees_df = trees_df.dropna(subset=["longitude", "latitude"])

st.title("Streamlit AgGrid Example: Tree")
AgGrid(trees_df)

st.write("AgGrid editable DataFrame:")
response = AgGrid(trees_df, height=500, editable=True)
df_edited = response["data"]
st.write("Edited DataFrame:")
st.dataframe(df_edited)

#pandas-profiling
# from pandas_profiling import ProfileReport
# from streamlit_pandas_profiling import st_profile_report

# tree_profile = ProfileReport(trees_df, explorative=True)
# st_profile_report(tree_profile)

#folium
import folium
from streamlit_folium import st_folium

st.title("SF Trees Map")
trees_df = trees_df.head(n=100)

lat_avg = trees_df["latitude"].mean()
lon_avg = trees_df["longitude"].mean()
m = folium.Map(location=[lat_avg, lon_avg], zoom_start=12)
for _, row in trees_df.iterrows():
    folium.Marker(
        [row["latitude"], row["longitude"]],
    ).add_to(m)

events = st_folium(m)
st.write(events)

#PLOTLY EVENTS
import plotly.express as px
from streamlit_plotly_events import plotly_events

#mapbox_access
#fig = px.scatter_mapbox(trees_df, lat="latitude", lon="longitude", color="legal_status")
#fig.update_layout(mapbox_style="open-street-map")
#st.plotly_chart(fig)

fig = px.scatter(trees_df, x="longitude", y="latitude", color="legal_status")
#plotly_events(fig)
selected_point = plotly_events(fig, click_event=True)
st.write("Selected point:")
st.write(selected_point)

if len(selected_point) == 0:
    st.stop()
selected_x_value = selected_point[0]["x"]
selected_y_value = selected_point[0]["y"]
df_selected = trees_df[
    (trees_df["longitude"] == selected_x_value)
    & (trees_df["latitude"] == selected_y_value)
]
st.write("Data for selected point:")
st.write(df_selected)

