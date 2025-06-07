import os
from dotenv import load_dotenv
from rag.loader import load_text_blobs
from azure.storage.blob import ContainerClient

load_dotenv()

AZURE_CONTAINER_URL = os.getenv("AZURE_BLOB_CONTAINER_URL")

container = ContainerClient.from_container_url(AZURE_CONTAINER_URL)
blobs = list(container.list_blobs())
print("📦 Blobs trouvés :", [b.name for b in blobs])  