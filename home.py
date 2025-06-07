import streamlit as st

def render():
    st.markdown("<h1 style='text-align: center;'>🏠 Welcome to <span style='color:#1f77b4;'>Data4Demo</span></h1>", unsafe_allow_html=True)
    st.write("Explore categorized documents, submit demandes, and view maps.")
    st.write("---")

    category = st.selectbox("🎯 Choose a category:", ["Politique", "Culturelle", "Administration", "Construction"])
    st.markdown(f"### 📰 Latest in **{category}**")
    st.info("No documents available yet. New uploads coming soon!")
