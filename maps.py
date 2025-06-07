import streamlit as st
from streamlit_folium import st_folium
import folium

def render():
    st.markdown("<h1 style='text-align:center;'>🗺️ Interactive Map</h1>", unsafe_allow_html=True)
    st.write("Explore the map to view key locations related to projects or demands.")
    st.write("---")

    location = [46.8182, 8.2275]  # Switzerland

    m = folium.Map(location=location, zoom_start=8, tiles="CartoDB positron")

    folium.Marker(
        location=[46.9480, 7.4474],
        popup="<b>Bern</b>",
        icon=folium.Icon(color='blue', icon="info-sign")
    ).add_to(m)

    st_folium(m, width=800, height=500)
