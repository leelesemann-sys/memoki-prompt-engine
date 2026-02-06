"""Prompt-Builder für Paare Memory.

Modus: Zusammengehörige Objekte bilden ein Paar
(z.B. TV & Fernbedienung, Schuh & Schnürsenkel).
"""


class PairsPromptBuilder:
    """Baut Prompts für den Paare-Memory-Modus."""

    def build_prompt(self, object_name: str, style: str = "cartoon") -> str:
        """Erstellt einen Bildgenerierungs-Prompt für ein Objekt.

        Args:
            object_name: Das darzustellende Objekt (z.B. "Fernbedienung").
            style: Bildstil.

        Returns:
            Prompt-String für den Bildgenerator.
        """
        raise NotImplementedError
