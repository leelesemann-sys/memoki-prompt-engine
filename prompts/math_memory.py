"""Prompt-Builder für Mathe Memory.

Modus: Karte A zeigt eine Zahl, Karte B zeigt ein Bild
mit der entsprechenden Menge an Objekten.
"""


class MathPromptBuilder:
    """Baut Prompts für den Mathe-Memory-Modus."""

    def build_prompt(self, number: int, style: str = "cartoon") -> str:
        """Erstellt einen Bildgenerierungs-Prompt für eine gegebene Zahl.

        Args:
            number: Die darzustellende Zahl (z.B. 5).
            style: Bildstil (z.B. "cartoon", "realistic").

        Returns:
            Prompt-String für den Bildgenerator.
        """
        raise NotImplementedError
