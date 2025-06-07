import os
import json


def list_blob_urls_from_local_metadata():
    """Charge les documents depuis un fichier metadata.json local à la racine du projet."""
    try:
        with open("metadata.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        # Vérifie que chaque élément est un dictionnaire avec les clés attendues
        if not isinstance(data, list):
            raise ValueError("Le fichier metadata.json doit contenir une liste de documents.")

        for doc in data:
            if not isinstance(doc, dict):
                raise ValueError("Chaque entrée dans metadata.json doit être un dictionnaire.")
            if "name" not in doc:
                raise ValueError("Chaque document doit avoir une clé 'name'.")
            if "tags" not in doc:
                doc["tags"] = []
            if "summary" not in doc:
                doc["summary"] = ""
            if "uploaded" not in doc:
                doc["uploaded"] = ""
            if "url" not in doc:
                # Génère un lien fictif ou utilise un chemin statique
                doc["url"] = f"https://your-container-url/{doc['name']}"

        return data

    except Exception as e:
        raise RuntimeError(f"Erreur lors du chargement de metadata.json : {e}")
