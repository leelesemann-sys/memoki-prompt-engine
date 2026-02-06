"""Zentrale Konfiguration für llm-semantic-memory.

Lädt API-Keys und Modell-Einstellungen aus .env-Datei.
"""

import os
from dotenv import load_dotenv

load_dotenv()

# Azure OpenAI (DALL-E 3)
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY", "")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT", "")
AZURE_OPENAI_DALLE_DEPLOYMENT = os.getenv("AZURE_OPENAI_DALLE_DEPLOYMENT", "dall-e-3")

# Google AI Studio (Gemini / Nano Banana Pro)
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")
GOOGLE_IMAGE_MODEL = "gemini-3-pro-image-preview"

# Spielfeld-Defaults
DEFAULT_PAIR_COUNT = 6  # Anzahl Kartenpaare
IMAGE_SIZE = "512x512"
