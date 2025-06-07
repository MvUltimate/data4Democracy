import streamlit as st

def render():
    st.markdown("<h1 style='text-align:center;'>📚 Shared Documents</h1>", unsafe_allow_html=True)
    st.write("Find the latest documents shared within each category.")
    st.write("---")

    docs = [
        {"title": "🏛️ Political Update", "category": "Politique"},
        {"title": "🎨 Cultural Events", "category": "Culturelle"},
        {"title": "🏗️ Construction Guidelines", "category": "Construction"},
        {"title": "📑 Admin Policies", "category": "Administration"}
    ]

    cols = st.columns(2)
    for i, doc in enumerate(docs):
        with cols[i % 2]:
            st.markdown(
                f"""
                <div class='doc-card'>
                    <h3>{doc['title']}</h3>
                    <span>📌 Category: {doc['category']}</span>
                </div>
                """,
                unsafe_allow_html=True
            )
