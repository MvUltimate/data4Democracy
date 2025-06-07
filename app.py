import streamlit as st

# ✅ MUST be the first Streamlit command
st.set_page_config(page_title="Data4Demo", layout="wide")

import home
import demande
import maps
import shared_docs
import about
import cantons

# Optional: inject custom CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def main():
    local_css("style.css")

    menu = st.sidebar.selectbox("Menu", ["🏠 Home", "📄 Demande", "🗺️ Maps", "🗂️ Shared Documents","🏛️ Cantons", "ℹ️ About"])

    if menu == "🏠 Home":
        home.render()

    elif menu == "📄 Demande":
        demande.render()

    elif menu == "🗺️ Maps":
        maps.render()

    elif menu == "🗂️ Shared Documents":
        shared_docs.render()

    elif menu == "ℹ️ About":
        import about
        about.render()
    elif menu == "🏛️ Cantons":
        import cantons  # You can rename this file to `cantons.py` for consistency
        cantons.render()

if __name__ == "__main__":
    main()
