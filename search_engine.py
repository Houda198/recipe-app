import requests
from bs4 import BeautifulSoup
from duckduckgo_search import DDGS
import re

def clean_html(html_content):
    """Nettoyage de données (Data Cleaning) via Regex et BS4"""
    soup = BeautifulSoup(html_content, 'html.parser')
    # Suppression des éléments inutiles (bruit de données)
    for element in soup(['script', 'style', 'nav', 'header', 'footer', 'aside']):
        element.decompose()
    
    text = soup.get_text(separator=' ')
    # Regex pour nettoyer les espaces multiples et caractères spéciaux
    text = re.sub(r'\s+', ' ', text).strip()
    return text[:2000] # On limite pour le contexte LLM

def get_automated_context(query):
    """Pipeline complet d'automatisation de la recherche"""
    raw_texts = []
    with DDGS() as ddgs:
        results = list(ddgs.text(f"{query} ingredients instructions", max_results=5))
        for r in results:
            try:
                resp = requests.get(r['href'], timeout=5)
                if resp.status_code == 200:
                    raw_texts.append(clean_html(resp.text))
            except:
                continue
    return raw_texts