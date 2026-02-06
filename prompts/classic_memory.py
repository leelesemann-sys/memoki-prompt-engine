"""Prompt-Builder für Classic Memory.

Modus: Beide Karten eines Paares zeigen das identische Motiv.
"""


class ClassicPromptBuilder:
    """Baut Prompts für den Classic-Memory-Modus."""

    def build_prompt(self, subject: str, style: str = "cartoon") -> str:
        """Erstellt einen Bildgenerierungs-Prompt für ein Motiv.

        Args:
            subject: Das darzustellende Motiv (z.B. "Katze").
            style: Bildstil (z.B. "cartoon", "realistic").

        Returns:
            Prompt-String für den Bildgenerator.
        """
        raise NotImplementedError
