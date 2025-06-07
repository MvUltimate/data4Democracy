# rag/loader.py

from azure.storage.blob import ContainerClient
from dotenv import load_dotenv
import os

load_dotenv()

AZURE_CONTAINER_URL = os.getenv("AZURE_BLOB_CONTAINER_URL")


def list_blob_urls() -> list[dict]:
    """Renvoie la liste des blobs sous forme de paires nom + URL."""
    container = ContainerClient.from_container_url(AZURE_CONTAINER_URL)
    blobs = []

    for blob in container.list_blobs():
        try:
            blob_url = f"{AZURE_CONTAINER_URL}/{blob.name}"
            # Ajout d'un résumé basique basé sur le nom du fichier
            summary = summarize_filename(blob.name)
            blobs.append({"name": blob.name, "url": blob_url, "summary": summary})
        except Exception as e:
            print(f"⚠️ Erreur lors de la génération de l'URL pour {blob.name} : {e}")

    return blobs


def summarize_filename(filename: str) -> str:
    """Génère un résumé simple basé sur le nom du fichier."""
    # Exemple de traitement très simple, à améliorer si besoin
    name = filename.replace("_", " ").replace(".pdf", "").replace(".xls", "").replace(".xlsx", "").replace(".csv", "")
    return f"Document : {name}"
