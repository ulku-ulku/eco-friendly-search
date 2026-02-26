import re
import streamlit as st

st.set_page_config(page_title="Eco Intent Search", page_icon="🌿")

# Fake mini catalog (NO is_eco_friendly field)
PRODUCTS = [
    {"id": 1, "name": "Bamboo Coffee Table", "price": 120,
     "description": "Modern coffee table made from sustainable bamboo and non-toxic finish."},
    {"id": 2, "name": "Classic Leather Sofa", "price": 850,
     "description": "Premium leather sofa with solid wood frame."},
    {"id": 3, "name": "Recycled Wood Shelf", "price": 300,
     "description": "Shelf made from recycled wood and eco-friendly varnish."},
    {"id": 4, "name": "Organic Paint Cabinet", "price": 420,
     "description": "Cabinet coated with organic paint and low-VOC materials."},
    {"id": 5, "name": "Plastic Outdoor Chair", "price": 60,
     "description": "Durable plastic chair for outdoor use."},
]

ECO_KEYWORDS = [
    "eco", "eco-friendly", "sustainable", "recycled",
    "non-toxic", "organic", "bamboo", "low-voc",
    "çevre dostu", "sürdürülebilir", "geri dönüştürülmüş"
]

def is_eco_text(text):
    text = text.lower()
    return any(word in text for word in ECO_KEYWORDS)

st.title("🌿 Free Text Search / Intent Extraction Demo")

query = st.text_input("Ne arıyorsunuz? (ör: çevre dostu, bamboo, sustainable)")

if query:
    query_lower = query.lower()

    # Eco intent detection
    eco_intent = any(word in query_lower for word in ECO_KEYWORDS)

    if eco_intent:
        st.subheader("✅ Eco Intent Detected")
        results = [p for p in PRODUCTS if is_eco_text(p["description"])]
    else:
        st.subheader("🔎 General Search")
        results = [
            p for p in PRODUCTS
            if query_lower in p["name"].lower()
            or query_lower in p["description"].lower()
        ]

    if results:
        for p in results:
            st.markdown(f"### {p['name']} - ${p['price']}")
            st.write(p["description"])
            st.write("---")
    else:
        st.warning("Sonuç bulunamadı.")
