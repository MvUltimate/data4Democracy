import streamlit as st
from rag.blob_utils import upload_file_to_blob

def render():
    st.markdown("<h1 style='text-align:center;'>📤 Uploader un document</h1>", unsafe_allow_html=True)
    st.write("Sélectionne un fichier à envoyer dans le conteneur Azure.")
    st.write("---")

    uploaded_file = st.file_uploader("📎 Choisir un fichier", type=None)

    if uploaded_file:
        filename = uploaded_file.name

        if st.button("🚀 Envoyer"):
            with st.spinner("📡 Envoi en cours..."):
                try:
                    upload_file_to_blob(uploaded_file, filename)
                    st.success(f"✅ Fichier « {filename} » envoyé avec succès !")
                except Exception as e:
                    st.error(f"❌ {e}")
