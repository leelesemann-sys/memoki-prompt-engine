# LLM Semantic Memory

Memory-Spiel-Generator mit KI-generierten Bildern. Ein Lern- und Portfolio-Projekt für LLM-Tuning, Prompt Engineering und Agentenorchestrierung.

## Spielmodi

- **Classic Memory** – Identische Bildpaare finden
- **Mathe Memory** – Zahl einer Menge zuordnen
- **Paare Memory** – Zusammengehörige Objekte finden
- **Teekesselchen Memory** – Homonyme erkennen

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
# .env mit eigenen API-Keys befüllen
streamlit run app.py
```

## Tech-Stack

- **Frontend:** Streamlit
- **Bildgeneratoren:** Azure DALL-E 3, Google Gemini (Nano Banana Pro)
- **Hosting:** Azure
