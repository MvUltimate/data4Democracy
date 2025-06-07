# 🧠 Assistant Citoyen Intelligent – RAG avec LangChain 🇨🇭

Ce projet est un prototype d’assistant numérique basé sur un modèle de langage (LLM) augmenté par la recherche documentaire (RAG – Retrieval-Augmented Generation). Il permet aux citoyens suisses de poser des questions et d’obtenir des réponses précises à partir de documents publics (PDF, textes, lois, budgets, etc.).

---

## 🚀 Fonctionnalités principales

- 🔍 Recherche intuitive et rapide dans les documents publics
- 🌍 Carte interactive pour explorer les lieux et données locales
- 🧠 Lecture et compréhension facilitées grâce à l’IA
- 📄 Génération automatique de demandes si un document n’existe pas
- 🆕 Suivi des nouveautés : nouveaux documents, nouveaux thèmes
- ✅ Accessible à tous : simple, rapide, inclusif

---

## 📦 Prérequis

- Python 3.8+
- Une clé OpenAI (si usage GPT-3.5/4)
- `pip` installé

---

## ⚙️ Installation

```bash
git clone https://github.com/ton-compte/assistant-citoyen-rag.git
cd assistant-citoyen-rag

# Optionnel : créer un environnement virtuel
python -m venv venv
.\venv\Scripts\activate       # Windows
source venv/bin/activate      # Mac/Linux

# Installer les dépendances
pip install -r requirements.txt
```

---

## 🔐 Configuration

Crée un fichier `.env` à la racine avec ta clé OpenAI :

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx
```

---

## 📁 Ajouter des documents

Place tes fichiers `.txt` ou `.pdf` dans le dossier `documents/`.  
Ils seront automatiquement pris en compte lors de l’indexation.

---

## 🧪 Lancer l’assistant

### 🖥️ Version console :
```bash
python run_rag.py
```
Puis pose une question comme :
> "Quel est le budget 2023 de la ville de Sion pour la culture ?"

---

## 💻 Interface web (optionnel avec Streamlit)

```bash
pip install streamlit
streamlit run app.py
```

---

## 🧭 Architecture fonctionnelle

```text
[Utilisateur] → pose une question
        ↓
     [Chat RAG]
    /         \
[Doc existe]  [Doc introuvable]
    ↓              ↓
Réponse + lien   Génération automatique
doc trouvé       d’une demande légale
                    ↓
             Envoi selon le canton
                    ↓
             Ajout dans la base une fois reçu
```

---

## 🔄 Cas d’usage : “Demande de document administratif”

**Acteur :** citoyenne ou citoyen  
**But :** obtenir un document (budget communal, procès-verbal, rapport)

### 🔁 Scénario :
1. L’utilisateur demande : _"Quel est le budget 2023 pour la culture à Sion ?"_
2. Le système cherche dans la base :
   - ✅ S’il existe → le lien et l'info sont fournis.
   - ❌ S’il n’existe pas → le système génère une **demande d'accès officielle**.
3. L’utilisateur est guidé pour soumettre la demande.
4. Une fois le document reçu, il est ajouté dans la base pour les prochaines personnes.

---

## 💡 Qui finance ?

- ✅ Réduction du travail des administrations (moins de redondance)
- ✅ Démarche alignée avec l’intérêt public
- 💰 Proposition : **financement public / subvention** pour transparence citoyenne

---

## 📚 Stack utilisée

- 🧱 [LangChain](https://www.langchain.com/)
- 🧠 OpenAI API (GPT-4 / GPT-3.5)
- 📚 ChromaDB ou FAISS (indexation vectorielle)
- 🛠️ Python, dotenv, tiktoken

---

## 📌 À faire / idées futures

- Support Mistral 7B (via Ollama ou LM Studio)
- UI avancée (Vue.js, Flask)
- Générateur automatique de demandes LTrans
- Analyse automatique des budgets cantonaux

---

## 👨‍💻 Auteur

> Projet créé pendant le [Hackathon Data4Democracy 2025 🇨🇭]  
> Réalisé par [Ton Nom / Équipe]

---

## 📄 Licence

Ce projet est sous licence MIT — libre d’usage, mais gardez les mentions !
