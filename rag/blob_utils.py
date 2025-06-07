import os
from azure.storage.blob import ContainerClient

AZURE_CONTAINER_SAS_URL = os.getenv("AZURE_BLOB_CONTAINER_WRITE_URL")  # Ceci est une URL avec un SAS token

def get_container_client():
    if not AZURE_CONTAINER_SAS_URL:
        raise ValueError("La variable d'environnement AZURE_BLOB_CONTAINER_WRITE_URL est manquante.")
    
    return ContainerClient.from_container_url(AZURE_CONTAINER_SAS_URL)

def upload_file_to_blob(file, filename):
    try:
        container_client = get_container_client()
        blob_client = container_client.get_blob_client(blob=filename)
        blob_client.upload_blob(file, overwrite=True)
        return True
    except Exception as e:
        raise RuntimeError(f"Erreur d'upload vers Azure : {e}")
