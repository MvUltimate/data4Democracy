import streamlit as st
from streamlit_folium import st_folium
import folium
from map_points import points

def render():
    # Remove Streamlit default padding/margin
    st.markdown("""
        <style>
        .block-container {
            padding: 0;
        }
        .main {
            padding: 0;
        }
        iframe {
            height: 100vh !important;
        }
        </style>
    """, unsafe_allow_html=True)

    # Fullscreen title (optional)
    st.markdown("<h1 style='text-align:center; margin-top: 10px;'>🗺️ Carte des infrastructures publiques</h1>", unsafe_allow_html=True)

    # Initialize Leaflet map
    m = folium.Map(location=[46.8182, 8.2275], zoom_start=7, tiles="CartoDB positron")

    icon_map = {
        "Bridge": ("blue", "road"),
        "Gym Building": ("green", "glyphicon-plus"),
        "Game Place": ("orange", "glyphicon-play"),
        "State Building": ("red", "glyphicon-home"),
        "Cultural Center": ("purple", "glyphicon-music")
    }

    for item in points:
        color, icon = icon_map.get(item["type"], ("gray", "info-sign"))
        doc_links = "<ul>" + "".join(
            f"<li><a href='{doc['url']}' target='_blank'>{doc['title']}</a></li>" for doc in item["docs"]
        ) + "</ul>"
        popup_content = f"""
            <b>{item['name']}</b><br>
            Type: {item['type']}<br><br>
            <b>📄 Documents liés:</b>{doc_links}
        """
        folium.Marker(
            location=item["location"],
            popup=folium.Popup(popup_content, max_width=300),
            icon=folium.Icon(color=color, icon=icon, prefix='glyphicon')
        ).add_to(m)

    # Display fullscreen map
    st_folium(m, width=None, height=800, use_container_width=True)
