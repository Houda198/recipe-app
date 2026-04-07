import pandas as pd
from sentence_transformers import SentenceTransformer, util
import torch

# Modèle ML 1 : Recherche Sémantique (SBERT)
# Il permet de trouver la recette la plus proche "mathématiquement" du besoin utilisateur
embedder = SentenceTransformer('all-MiniLM-L6-v2')

def rank_best_recipes(user_query, scraped_data):
    """
    ML Logic: Calcule la similarité cosinus entre la requête et les résultats web
    pour filtrer le 'bruit' et ne garder que la haute qualité.
    """
    if not scraped_data: return ""
    
    # Encodage de la requête et des textes scrappés
    query_embedding = embedder.encode(user_query, convert_to_tensor=True)
    corpus_embeddings = embedder.encode(scraped_data, convert_to_tensor=True)
    
    # Calcul des scores de similarité
    hits = util.semantic_search(query_embedding, corpus_embeddings, top_k=2)
    
    # On ne garde que les sources avec un score > 0.4 (Nettoyage intelligent)
    best_context = ""
    for hit in hits[0]:
        best_context += scraped_data[hit['corpus_id']] + "\n"
    
    return best_context