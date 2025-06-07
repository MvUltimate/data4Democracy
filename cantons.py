import streamlit as st
from streamlit_image_select import image_select
from database import get_connection

# Dictionary of canton names and paths to their flag icons
CANTONS = {
    "Bern": "canton_icons/Flag_of_Canton_of_Bern.svg.png",
    "Fribourg": "canton_icons/Flag_of_Canton_of_Fribourg.svg.png",
    "Glarus": "canton_icons/Flag_of_Canton_of_Glarus.svg.png",
    "Graubünden": "canton_icons/Flag_of_Canton_of_Graubünden.svg.png",
    "Sankt Gallen": "canton_icons/Flag_of_Canton_of_Sankt_Gallen.svg.png",
    "Schwyz": "canton_icons/Flag_of_Canton_of_Schwyz.svg.png",
    "Uri": "canton_icons/Flag_of_Canton_of_Uri.svg.png",
    "Valais": "canton_icons/Flag_of_Canton_of_Valais.svg.png"
}

# Transparency info for each canton
CANTON_INFO = {
    "Bern": {
        "info": "Bern follows the IDG for transparency and citizen access.",
        "documents": ["IDG Law (PDF)", "Mandate Structure", "Transparency Guidelines"]
    },
    "Fribourg": {
        "info": "Fribourg applies LInfA and handles access on demand.",
        "documents": ["LInfA Framework", "Public Info Act", "Appeal Process Doc"]
    },
    "Glarus": {
        "info": "Glarus emphasizes public participation through local law.",
        "documents": ["Local Participation Charter", "FOI Regulations"]
    },
    "Graubünden": {
        "info": "Graubünden supports public transparency via cantonal law.",
        "documents": ["Transparency Ordinance", "Grants Disclosure"]
    },
    "Sankt Gallen": {
        "info": "St. Gallen provides data under DSG and openness policies.",
        "documents": ["DSG Act", "Public Access Order", "Responsibility Matrix"]
    },
    "Schwyz": {
        "info": "Schwyz responds to written requests within 30 days.",
        "documents": ["Administrative Access Law", "Request Handling Policy"]
    },
    "Uri": {
        "info": "Uri offers limited transparency under Verwaltungsrechtspflegegesetz.",
        "documents": ["VRPG Article", "Transparency Restrictions"]
    },
    "Valais": {
        "info": "Valais grants access to administrative documents upon request.",
        "documents": ["Valais Info Access Act", "Request Form Template"]
    }
}

def render():
    st.markdown("<h1 style='text-align:center;'>🏛️ Choose Your Canton</h1>", unsafe_allow_html=True)
    st.write("---")

    canton_names = list(CANTONS.keys())
    image_paths = list(CANTONS.values())

    selected_image = image_select(
        label="Click on a flag to select a canton",
        images=image_paths,
        captions=canton_names,
        use_container_width=False
    )

    selected = next((name for name, path in CANTONS.items() if path == selected_image), None)
    st.session_state.selected_canton = selected

    if selected:
        st.markdown(f"### 🧾 Transparency Info for *{selected}*")
        st.info(CANTON_INFO.get(selected, "Information not available."))

        st.markdown("### ✍️ Submit a Request")

        with st.form("canton_request_form", clear_on_submit=True):
            office_nom = st.selectbox("🏢 Office concerné par la demande de document", [
                "Office fédéral de la santé publique (OFSP)",
                "Office fédéral de la statistique (OFS)",
                "Office fédéral de la police (fedpol)",
                "Canton de Vaud – Département de la formation",
                "Canton du Valais – Département de la sécurité",
                "Office fédéral des transports (OFT)"
            ])
            subject = st.text_input("Subject of your request")
            description = st.text_area("Describe what you're requesting")
            contact = st.text_input("Your email or contact info")
            submitted = st.form_submit_button("📤 Submit Request")

            if submitted:
                try:
                    conn = get_connection()
                    cursor = conn.cursor()

                    cursor.execute("SELECT ID FROM Services WHERE Nom_Service = ?", (office_nom,))
                    row = cursor.fetchone()

                    if row:
                        office_id = row[0]

                        cursor.execute("""
                            INSERT INTO RequetesUtilisateurs (ServiceID, RequeteTexte, Document)
                            VALUES (?, ?, ?)
                        """, (office_id, description, "En cours"))
                        conn.commit()

                        st.success(f"✅ Your request to *{selected}* has been submitted and saved.")
                    else:
                        st.error("❌ Office introuvable dans la base.")

                except Exception as db_error:
                    st.error(f"❌ Erreur base de données : {db_error}")
                finally:
                    conn.close()
