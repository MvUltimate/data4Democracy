import streamlit as st
from rag.local_loader import list_blob_urls_from_local_metadata
import json


def render():
    st.markdown("<h1 style='text-align:center;'>📚 Shared Documents</h1>", unsafe_allow_html=True)
    st.write("Clique sur une catégorie pour voir les documents publics associés.")
    st.write("---")

    # Chargement robuste
    try:
        blobs = list_blob_urls_from_local_metadata()
        # Si le fichier est une liste brute, le convertir en liste de dicts avec clés attendues
        if isinstance(blobs, list) and all(isinstance(item, list) for item in blobs):
            raise ValueError("Le fichier metadata contient une liste de listes au lieu d'une liste de dictionnaires.")
    except Exception as e:
        st.error(f"Erreur de chargement des documents : {e}")
        return

    categories = {
        "culturelle": "🎨 Culturelle",
        "politique": "🏛️ Politique",
        "administration": "📑 Administration",
        "construction": "🏗️ Construction"
    }

    # Initialisation de l'état sélectionné
    if "selected_tag" not in st.session_state:
        st.session_state.selected_tag = None

    st.subheader("📂 Catégories")
    num_per_row = 2
    keys = list(categories.keys())

    for i in range(0, len(keys), num_per_row):
        row = keys[i:i + num_per_row]
        cols = st.columns(len(row))
        for col, tag in zip(cols, row):
            if col.button(categories[tag]):
                st.session_state.selected_tag = tag

    selected_tag = st.session_state.selected_tag

    if selected_tag:
        st.markdown(f"### 📂 Documents dans la catégorie **{categories[selected_tag]}**")

        # Vérification du contenu
        valid_blobs = []
        for b in blobs:
            if isinstance(b, dict) and "tags" in b and isinstance(b["tags"], list):
                # Recréer l'URL si absente (basé sur un container fictif)
                b.setdefault("url", f"https://your-container-url/{b['name']}")
                valid_blobs.append(b)

        filtered = [
            b for b in valid_blobs
            if any(tag.lower() == selected_tag.lower() for tag in b.get("tags", []))
        ]
        filtered.sort(key=lambda b: b.get("uploaded", ""), reverse=True)

        if not filtered:
            st.info("Aucun document trouvé pour cette catégorie.")
        else:
            for blob in filtered:
                st.markdown(f"""
                <div style="padding: 1rem; border-radius: 0.5rem; background-color: #f9f9f9; margin-bottom: 1rem;">
                    <h4 style="margin-bottom: 0.3rem;">📄 {blob['name']}</h4>
                    <p style="margin: 0.2rem 0;">🗓️ {blob.get("uploaded", "Date inconnue")}</p>
                    <p style="margin: 0.2rem 0;">📝 {blob.get("summary", "Pas de résumé")}</p>
                    <a href="{blob['url']}" target="_blank">🔗 Ouvrir le document</a>
                </div>
                """, unsafe_allow_html=True)
