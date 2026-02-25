<<<<<<< HEAD
import streamlit as st

# Fake product catalog (No structured eco field!)
products = [
    {
        "id": 1,
        "name": "Bamboo Coffee Table",
        "price": 120,
        "description": "Modern coffee table made from sustainable bamboo material and non-toxic finish."
    },
    {
        "id": 2,
        "name": "Classic Leather Sofa",
        "price": 850,
        "description": "Premium Italian leather sofa with solid wood frame."
    },
    {
        "id": 3,
        "name": "Recycled Wood Bookshelf",
        "price": 300,
        "description": "Bookshelf made from recycled wood and eco-friendly varnish."
    },
    {
        "id": 4,
        "name": "Plastic Outdoor Chair",
        "price": 60,
        "description": "Durable plastic chair suitable for outdoor use."
    }
]

eco_keywords = [
    "eco", "sustainable", "recycled",
    "organic", "non-toxic", "bamboo"
]

def is_eco_query(user_input):
    user_input = user_input.lower()
    return any(word in user_input for word in eco_keywords)

def is_eco_product(description):
    description = description.lower()
    return any(word in description for word in eco_keywords)

st.title("AI Furniture Assistant")

query = st.text_input("Ne arıyorsunuz? (örn: çevre dostu ürünler)")

if query:
    if is_eco_query(query):
        st.subheader("🌱 Çevre Dostu Ürünler")
        found = False
        for product in products:
            if is_eco_product(product["description"]):
                st.write(f"**{product['name']}** - ${product['price']}")
                st.write(product["description"])
                st.write("---")
                found = True
        if not found:
            st.write("Çevre dostu ürün bulunamadı.")
    else:
        st.subheader("Tüm Ürünler")
        for product in products:
            st.write(f"**{product['name']}** - ${product['price']}")
            st.write(product["description"])
            st.write("---")
