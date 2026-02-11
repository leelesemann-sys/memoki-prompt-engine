"""Zentrale Konfiguration für llm-semantic-memory.

Lädt API-Keys und Modell-Einstellungen aus .env-Datei.
"""

import os
from dotenv import load_dotenv

load_dotenv()

# Google AI Studio (Gemini)
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")
GOOGLE_CHAT_MODEL = "gemini-2.5-flash"  # Text-Chat für MEMOKI Agent
GOOGLE_IMAGE_MODEL = "gemini-3-pro-image-preview"
GOOGLE_IMAGE_MODEL_FAST = "gemini-2.5-flash-image"  # Fallback für Mathe-Karten

# Spielfeld-Defaults
DEFAULT_PAIR_COUNT = 6  # Anzahl Kartenpaare
IMAGE_SIZE = "1024x1024"
