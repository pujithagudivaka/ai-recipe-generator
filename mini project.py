import streamlit as st

st.set_page_config(page_title="AI Recipe Generator", page_icon="🍲")

st.title("🍲 Personalized AI Recipe Generator")
st.write("Generate recipes using the ingredients you have!")

ingredients = st.text_input(
    "Enter your ingredients",
    placeholder="e.g. tomato, onion, potato"
)

diet = st.selectbox(
    "Choose your food preference",
    ["Vegetarian", "Vegan", "Non-Vegetarian"]
)

if st.button("Generate Recipe"):
    if ingredients.strip():
        st.subheader("Your Recipe")
        st.write("**Ingredients:**", ingredients)
        st.write("**Food preference:**", diet)
        st.write("**Preparation:**")
        st.write("1. Wash and prepare your ingredients.")
        st.write("2. Cook them with suitable spices and seasoning.")
        st.write("3. Cook until ready and serve hot!")
    else:
        st.warning("Please enter your ingredients first.")