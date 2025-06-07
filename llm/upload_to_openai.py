# llm/upload_to_openai.py

import os
import openai
from azure.storage.blob import ContainerClient
from dotenv import load_dotenv
from io import BytesIO
import time

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
AZURE_CONTAINER_URL = os.getenv("AZURE_BLOB_CONTAINER_URL")


def get_blob_bytes(blob_name: str) -> bytes:
    container = ContainerClient.from_container_url(AZURE_CONTAINER_URL)
    blob = container.get_blob_client(blob_name)
    return blob.download_blob().readall()


def upload_blob_to_openai(blob_name: str) -> str:
    blob_bytes = get_blob_bytes(blob_name)

    file = openai.files.create(
        file=BytesIO(blob_bytes),
        purpose="assistants",
    )
    return file.id


def ask_about_file(blob_name: str, prompt: str) -> str:
    blob_bytes = get_blob_bytes(blob_name)

    file = openai.files.create(
        file=BytesIO(blob_bytes),
        purpose="assistants"
    )

    assistant = openai.beta.assistants.create(
        name="Analyseur de documents publics suisses",
        instructions="Tu analyses les documents envoyés par l'utilisateur.",
        tools=[{"type": "file_search"}],
        model="gpt-4-turbo"
    )

    thread = openai.beta.threads.create()

    # ✅ Crée un message sans file_ids
    openai.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=prompt
    )

    # ✅ Les fichiers doivent être passés ici dans `run`
    run = openai.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant.id,
        tool_choice="file_search",
    )

    # Attente de la réponse
    while True:
        run_status = openai.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
        if run_status.status == "completed":
            break
        elif run_status.status == "failed":
            raise Exception("Échec de l'analyse.")
        time.sleep(2)

    messages = openai.beta.threads.messages.list(thread_id=thread.id)
    return messages.data[0].content[0].text.value

