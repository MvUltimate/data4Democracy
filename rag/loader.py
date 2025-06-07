# rag/loader.py

from azure.storage.blob import ContainerClient
from dotenv import load_dotenv
import os
import json

load_dotenv()

AZURE_CONTAINER_URL = os.getenv("AZURE_BLOB_CONTAINER_URL")


def list_blob_urls() -> list[dict]:
    """Renvoie la liste des blobs avec leurs tags depuis metadata.json s'ils existent."""
    container = ContainerClient.from_container_url(AZURE_CONTAINER_URL)
    blobs = []

    try:
        blob_list = container.list_blobs()
        for blob in blob_list:
            print(blob.name)  # ✅ Affiche uniquement le nom du fichier
    except Exception as e:
        print(f"Erreur lors du listage des blobs : {e}")

    return [{"name": blob.name} for blob in container.list_blobs()]


def summarize_filename(filename: str) -> str:
    """Génère un résumé simple basé sur le nom du fichier."""
    name = filename.replace("_", " ")\
                   .replace(".pdf", "")\
                   .replace(".xls", "")\
                   .replace(".xlsx", "")\
                   .replace(".csv", "")
    return f"Document : {name}"


def filter_blobs_by_query(blobs: list[dict], query: str) -> list[dict]:
    """Filtre les blobs en fonction du contenu de leur summary ou tags."""
    query_lower = query.lower()
    return [b for b in blobs if query_lower in b["summary"].lower() or any(query_lower in tag.lower() for tag in b.get("tags", []))]
