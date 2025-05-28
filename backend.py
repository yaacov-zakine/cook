import requests
import os

# La clé API est récupérée via les Secrets Streamlit Cloud
API_KEY = os.getenv("SPOONACULAR_API_KEY")
BASE_URL = "https://api.spoonacular.com/recipes/findByIngredients"

def get_recipes(ingredients, number=5, ranking=1):
    params = {
        "ingredients": ingredients,
        "number": number,
        "apiKey": API_KEY,
        "ranking": ranking
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Erreur API ({response.status_code}) : {response.text}")