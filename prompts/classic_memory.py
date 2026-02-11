"""Prompt-Builder für Classic Memory.

Modus: Beide Karten eines Paares zeigen das identische Motiv.
Nutzt die Stil- und Zielgruppen-Mappings aus tools/image.py.
"""

from tools.image import build_image_prompt


class ClassicPromptBuilder:
    """Baut Prompts für den Classic-Memory-Modus."""

    def __init__(self, style: str = "cartoon", audience: str = "children"):
        self.style = style
        self.audience = audience

    def build_prompt(self, subject: str) -> str:
        """Erstellt einen Bildgenerierungs-Prompt für ein Motiv.

        Args:
            subject: Das darzustellende Motiv (englisch, z.B. "elephant").

        Returns:
            Prompt-String für den Bildgenerator.
        """
        return build_image_prompt(subject, self.style, self.audience)
