from azure.storage.blob import ContainerClient
from dotenv import load_dotenv
import os

from rag.loader import is_text_blob

load_dotenv()

AZURE_CONTAINER_URL = os.getenv("AZURE_BLOB_CONTAINER_URL")

def test_blob_access():
    container = ContainerClient.from_container_url(AZURE_CONTAINER_URL)
    blobs = list(container.list_blobs())
    print(f"📦 {len(blobs)} blobs trouvés dans le container.")
    for blob in blobs:
        print(f"📝 {blob.name}")
        try:
            if is_text_blob(blob.name):
                try:
                    content = blob_data.decode("utf-8")
                except UnicodeDecodeError:
                    try:
                        content = blob_data.decode("latin-1")
                    except Exception as e:
                        print(f"❌ Erreur de décodage texte {blob.name} : {e}")
                        content = ""
                if content.strip():
                    print(f"📄 Taille du contenu : {len(content)} caractères")
        except Exception as e:
            print(f"⚠️ Erreur de lecture pour {blob.name} : {e}")

if __name__ == "__main__":
    test_blob_access()
