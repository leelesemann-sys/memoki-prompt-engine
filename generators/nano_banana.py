"""Google Nano Banana Pro (Gemini) Bildgenerator."""

from PIL import Image

from generators.base import ImageGenerator


class NanoBananaGenerator(ImageGenerator):
    """Generiert Bilder über Google AI Studio (Gemini)."""

    def __init__(self):
        # TODO: Google GenAI Client initialisieren
        pass

    def generate(self, prompt: str) -> Image.Image:
        """Generiert ein Bild mit Gemini (Nano Banana Pro)."""
        raise NotImplementedError("Nano Banana Generator noch nicht implementiert")
