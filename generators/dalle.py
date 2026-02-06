"""Azure DALL-E 3 Bildgenerator."""

from PIL import Image

from generators.base import ImageGenerator


class DalleGenerator(ImageGenerator):
    """Generiert Bilder über Azure OpenAI DALL-E 3."""

    def __init__(self):
        # TODO: Azure OpenAI Client initialisieren
        pass

    def generate(self, prompt: str) -> Image.Image:
        """Generiert ein Bild mit DALL-E 3."""
        raise NotImplementedError("DALL-E Generator noch nicht implementiert")
