import requests
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.environ["SPOONACULAR_API_KEY"]


BASE_URL = "https://api.spoonacular.com/recipes/findByIngredients"

def get_recipes(ingredients, number=5):
    params = {
        "ingredients": ingredients,
        "number": number,
        "apiKey": API_KEY,
        "ranking": 1
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Erreur lors de l'appel à l'API Spoonacular")
