import streamlit as st

def render():
    st.markdown("<h1 style='text-align: center;'>ℹ️ About Data4Demo</h1>", unsafe_allow_html=True)
    st.write("---")

    st.markdown("""
    **Data4Demo** is a citizen-focused platform designed to make **administrative and public documents** easily accessible to everyone.

    ### 🎯 Our Mission:
    - Promote **transparency** in public operations
    - Encourage **open access** to government and administrative data
    - Help users explore and understand public policies, decisions, and development projects

    ### 📂 What you can do with this app:
    - 🗂️ Browse shared documents across multiple themes like *politique, culturelle, administration,* and *construction*
    - 📄 Submit formal demandes (requests)
    - 🗺️ View map-based locations related to projects or document origins

    > Because information belongs to the people — not the filing cabinet.

    """)
