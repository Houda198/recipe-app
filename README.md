#  Chef IA Prestige : Pipeline RAG & Recherche Sémantique

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red.svg)
![NLP](https://img.shields.io/badge/NLP-Sentence--Transformers-green.svg)
![LLM](https://img.shields.io/badge/LLM-Llama3--Groq-orange.svg)

##  Présentation du Projet
Ce projet est un **Système Expert de Génération de Recettes** basé sur une architecture **RAG (Retrieval-Augmented Generation)**. Contrairement à une IA classique qui "invente" des recettes, ce système va chercher, nettoyer et valider des données réelles sur le web avant de les synthétiser.

##  Architecture Technique (Data Science)
Le projet repose sur 4 piliers technologiques :

1. **Extraction de Données (Data Engineering)** : Scraping automatisé via `DuckDuckGo Search` et nettoyage des données non structurées avec `BeautifulSoup4` et `Regex`.
2. **Recherche Sémantique (Machine Learning)** : Utilisation du modèle **SBERT (`all-MiniLM-L6-v2`)** pour vectoriser les résultats web et calculer une similarité cosinus avec la requête utilisateur.
3. **Optimisation du Contexte (Prompt Engineering)** : Injection des sources les plus pertinentes dans le "System Prompt" pour minimiser les hallucinations du modèle.
4. **Inférence Haute Performance** : Utilisation de l'API Groq (Llama 3) pour une génération de texte ultra-rapide en streaming.

##  Installation
```bash
# Cloner le projet
git clone [https://github.com/ton-pseudo/chef-ia-prestige.git](https://github.com/ton-pseudo/chef-ia-prestige.git)

# Installer les dépendances
pip install -r requirements.txt