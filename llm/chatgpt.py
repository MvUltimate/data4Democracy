
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_admin_response(prompt):
    try:

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": """
                 Tu es un assistant numérique citoyen suisse.
                 Tu as accès à un Azure Blob Storage contenant des documents publics suisses (budgets, lois, procès-verbaux, rapports, etc.).
                 Tu es capable de comprendre et d'analyser ces documents pour répondre aux questions des utilisateurs.
                 Lis les documents fournis par le système et utilise-les pour répondre aux questions de manière précise et factuelle.

                    Ta mission est d’aider les utilisateurs à :
                    - Chercher des documents dans le blob Azure qui correspondent à leur demande
                    - Comprendre des documents publics (budgets, lois, procès-verbaux, rapports, etc.)
                    - Répondre à des questions à partir des documents fournis par le système (tu ne dois pas inventer)
                    - Si les documents ne permettent pas de répondre, proposer une **demande administrative conforme à la LTrans**
                    - Rédiger cette demande de manière **formelle**, **claire** et **polie**

                    Utilise un ton professionnel, bienveillant, et transparent. Si une information est absente, propose une formulation à envoyer à une administration suisse pour demander le document concerné.

                    Tu réponds toujours en fonction de la langue du prompt de l'utilisateur.        
                """},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Erreur lors de l'appel à l'API : {e}"
