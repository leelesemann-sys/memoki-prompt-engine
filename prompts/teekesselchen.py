"""Prompt-Builder für Teekesselchen Memory.

Modus: Homonyme – zwei Bilder zeigen verschiedene Bedeutungen
desselben Wortes (z.B. "Eis" zum Essen + "Eis" im Winter).
"""

from tools.image import build_image_prompt


class TeekesselchenPromptBuilder:
    """Baut Prompts für den Teekesselchen-Memory-Modus."""

    def __init__(self, style: str = "cartoon", audience: str = "children"):
        self.style = style
        self.audience = audience

    def build_prompt(self, meaning_en: str) -> str:
        """Erstellt einen Bildgenerierungs-Prompt für eine Wort-Bedeutung.

        Args:
            meaning_en: Englische Beschreibung der Bedeutung
                        (z.B. "wooden park bench in a park").

        Returns:
            Prompt-String für den Bildgenerator.
        """
        return build_image_prompt(meaning_en, self.style, self.audience)
