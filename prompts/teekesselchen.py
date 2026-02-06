"""Prompt-Builder für Teekesselchen Memory.

Modus: Homonyme – zwei Bilder zeigen verschiedene Bedeutungen
desselben Wortes (z.B. "Eis" zum Essen + "Eis" im Winter).
"""


class TeekesselchenPromptBuilder:
    """Baut Prompts für den Teekesselchen-Memory-Modus."""

    def build_prompt(self, word: str, meaning: str, style: str = "cartoon") -> str:
        """Erstellt einen Bildgenerierungs-Prompt für eine Wort-Bedeutung.

        Args:
            word: Das Homonym (z.B. "Eis").
            meaning: Die spezifische Bedeutung (z.B. "Speiseeis").
            style: Bildstil.

        Returns:
            Prompt-String für den Bildgenerator.
        """
        raise NotImplementedError
