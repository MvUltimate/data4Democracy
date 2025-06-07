# demande.py

import streamlit as st
from llm.chatgpt import generate_admin_response
from llm.upload_to_openai import ask_about_file
from rag.loader import list_blob_urls


def render():
    st.markdown("<h1 style='text-align:center;'>📄 Créer une demande administrative</h1>", unsafe_allow_html=True)
    st.write("Complète le formulaire ci-dessous pour chercher un document ou générer une demande conforme à la LTrans.")
    st.write("---")

    # Sélection du fichier (optionnel)
    blob_list = list_blob_urls()
    blob_names = [b["name"] for b in blob_list]
    selected_blob = st.selectbox("📁 Fichier (optionnel)", ["-- Aucun --"] + blob_names)

    with st.form("demande_form", clear_on_submit=True):
        description = st.text_area("📖 Description", placeholder="Explique ce que tu cherches, pourquoi.")
        submit = st.form_submit_button("🚀 Générer la demande")

        if submit:
            if not description:
                st.warning("Merci de remplir tous les champs.")
                return

            user_query = f"{description}"
            print(f"🔍 Recherche pour : {user_query}")

            with st.spinner("🔍 Recherche en cours..."):

                if selected_blob != "-- Aucun --":
                    # 🔄 Envoie du fichier à OpenAI
                    with st.spinner(f"📡 Envoi du fichier « {selected_blob} » à ChatGPT..."):
                        try:
                            prompt = f"""
                                Tu es un assistant administratif suisse. L'utilisateur souhaite comprendre ou exploiter le document joint.

                                Question de l'utilisateur :
                                {user_query}

                                Analyse le document en pièce jointe pour y répondre de manière précise, factuelle et concise. Si le document ne contient pas d'information suffisante, indique-le.
                                """
                            response = ask_about_file(selected_blob, prompt)
                            st.success("✅ Réponse basée sur le fichier :")
                            st.write(response)
                        except Exception as e:
                            st.error(f"❌ Erreur lors de l'analyse du fichier : {e}")
                    return

                    prompt = f"\n\nUtilisateur : {user_query}\n\nGénère une demande formelle destinée à une administration suisse, conforme à la LTrans."

                    with st.spinner("✍️ Rédaction de la demande..."):
                        demande = generate_admin_response(prompt)

                    st.success("✅ Demande générée :")
                    st.code(demande, language="markdown")
