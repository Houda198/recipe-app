import os
from dotenv import load_dotenv
from groq import Groq
import streamlit as st 

# 1. On charge les variables du fichier .env dans la mémoire de Python
load_dotenv() 

# 2. On récupère la clé depuis l'environnement
api_key = st.secrets.get("GROQ_API_KEY") or os.environ.get("GROQ_API_KEY")

# 3. On initialise le client
client = Groq(api_key=api_key)

def generate_recipe_stream(prompt: str, system_prompt: str = "Tu es un chef étoilé..."):
    """
    Génère une recette via l'API Groq (Llama-3.3-70B).
    """
    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            stream=True
        )

        for chunk in completion:
            if chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content
    except Exception as e:
        yield f"Erreur technique : {str(e)}"