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

    # Télécharge le fichier metadata.json
    try:
        metadata_blob = container.get_blob_client("metadata.json")
        metadata_content = metadata_blob.download_blob().readall()
        metadata_dict = json.loads(metadata_content)
    except Exception as e:
        print(f"⚠️ Impossible de charger metadata.json : {e}")
        metadata_dict = {}

    for blob in container.list_blobs():
        try:
            blob_url = f"{AZURE_CONTAINER_URL}/{blob.name}"
            tags = metadata_dict.get(blob.name, {}).get("tags", [])
            summary = summarize_filename(blob.name)
            blobs.append({
                "name": blob.name,
                "url": blob_url,
                "summary": summary,
                "tags": tags
            })
        except Exception as e:
            print(f"⚠️ Erreur lors du traitement du blob {blob.name} : {e}")

    return blobs


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
