import streamlit as st

def render():
    st.markdown("<h1 style='text-align:center;'>📄 Submit a Demande</h1>", unsafe_allow_html=True)
    st.write("Please fill out the form below to submit your request.")
    st.write("---")

    with st.form("demande_form", clear_on_submit=True):
        title = st.text_input("🖊️ Title", placeholder="Enter title here...")
        description = st.text_area("📖 Description", placeholder="Describe your demande...")

        submit = st.form_submit_button("🚀 Submit")

        if submit:
            st.success("✅ Your demande has been submitted successfully!")
