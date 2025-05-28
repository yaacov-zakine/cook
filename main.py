import streamlit as st
from backend import get_recipes

st.title("🥗 MoodChef : Que cuisiner selon ton humeur ?")

# Étape 1 : Choix de l'humeur
mood = st.radio("Quelle est ton humeur aujourd'hui ?", [
    "Heureux(se)", "Stressé(e)", "Fatigué(e)", "Motivé(e)", "Envie de sucré"])

# Étape 2 : Ingrédients disponibles
ingredients = st.text_input("Liste les ingrédients que tu as (séparés par des virgules)", "poulet, tomates, riz")

# Étape 3 : Restrictions ou préférences alimentaires
diet = st.selectbox("As-tu un régime alimentaire particulier ?", [
    "Aucun", "Végétarien", "Vegan", "Sans gluten", "Halal"])

# Bouton pour lancer la recherche
if st.button("Trouver une recette"):
    if not ingredients:
        st.warning("Merci d'entrer au moins un ingrédient.")
    else:
        try:
            recipes = get_recipes(ingredients)
            if recipes:
                st.success(f"Voici {len(recipes)} recette(s) adaptée(s) à ton humeur '{mood}'")
                for r in recipes:
                    st.subheader(r['title'])
                    st.image(r['image'], width=300)
                    st.write(f"🧾 Ingrédients utilisés : {', '.join([i['name'] for i in r['usedIngredients']])}")
                    st.write(f"🛒 Ingrédients manquants : {', '.join([i['name'] for i in r['missedIngredients']])}")
                    st.markdown(f"[Voir la recette complète](https://spoonacular.com/recipes/{r['title'].replace(' ', '-')}-{r['id']})")
            else:
                st.info("Aucune recette trouvée avec ces ingrédients.")
        except Exception as e:
            st.error(str(e))
