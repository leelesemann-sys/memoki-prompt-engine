"""LLM Semantic Memory – Streamlit Hauptanwendung.

Memory-Spiel-Generator mit KI-generierten Bildern.
"""

import streamlit as st

st.set_page_config(
    page_title="LLM Semantic Memory",
    page_icon="🧠",
    layout="wide",
)

st.title("LLM Semantic Memory")
st.markdown("Memory-Spiel mit KI-generierten Bildern")

# Spielmodus-Auswahl
mode = st.selectbox(
    "Spielmodus wählen:",
    ["Classic Memory", "Mathe Memory", "Paare Memory", "Teekesselchen Memory"],
)

st.info(f"Modus **{mode}** ausgewählt – Bildgenerierung kommt in Schritt 2!")
