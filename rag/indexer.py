# rag/indexer.py
from langchain_community.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.schema import Document


# rag/indexer.py
from langchain_community.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.schema import Document

def build_vectorstore(documents: list[dict]) -> FAISS:
    # Filtrer les documents non vides
    langchain_docs = [
        Document(page_content=doc["content"], metadata={"name": doc["name"]})
        for doc in documents
        if doc.get("content", "").strip()  # contenu non vide
    ]

    if not langchain_docs:
        raise ValueError("Aucun document valide à indexer. Vérifie le contenu des blobs Azure.")

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(langchain_docs, embeddings)
    return vectorstore


