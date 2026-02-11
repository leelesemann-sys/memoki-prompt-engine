"""MEMOKI Agent – Chat-Orchestrierung mit Gemini.

Der Agent führt den User durch den Memory-Erstellungsprozess:
1. Informationen sammeln (Modus, Thema, Stil, Zielgruppe)
2. Zusammenfassung bestätigen lassen
3. Generation auslösen (via JSON-Action-Block)
"""

import json
from google import genai
from google.genai import types

from config.settings import GOOGLE_API_KEY, GOOGLE_CHAT_MODEL
from i18n import t


class MemokiAgent:
    """Chat-Agent der den User durch die Memory-Erstellung führt."""

    def __init__(self, mode: str, pair_count: int, lang: str = "de"):
        self.client = genai.Client(api_key=GOOGLE_API_KEY)
        self.mode = mode
        self.pair_count = pair_count
        self.lang = lang
        self.history: list[dict] = []

    def chat(self, user_message: str) -> str:
        """Sendet eine Nachricht an MEMOKI und gibt die Antwort zurück."""
        self.history.append({"role": "user", "parts": [{"text": user_message}]})

        # System-Prompt mit Kontext anreichern
        system_prompt = t("agent.system_prompt")
        context_header = t("agent.context_header", mode=self.mode, pair_count=self.pair_count)
        system = f"{system_prompt}\n\n{context_header}"

        response = self.client.models.generate_content(
            model=GOOGLE_CHAT_MODEL,
            contents=self.history,
            config=types.GenerateContentConfig(
                system_instruction=system,
                temperature=0.7,
            ),
        )

        assistant_text = response.text
        self.history.append({"role": "model", "parts": [{"text": assistant_text}]})
        return assistant_text

    @staticmethod
    def parse_action(text: str) -> dict | None:
        """Extrahiert einen JSON-Action-Block aus der Agent-Antwort.

        Returns:
            Dict mit action-Daten oder None wenn kein Action-Block gefunden.
        """
        if "```json" not in text:
            return None

        try:
            start = text.index("```json") + 7
            end = text.index("```", start)
            json_str = text[start:end].strip()
            data = json.loads(json_str)
            if data.get("action") == "generate":
                return data
        except (ValueError, json.JSONDecodeError):
            pass

        return None
