"""Abstract Base Class für Bildgeneratoren.

Jeder Bildgenerator (DALL-E, Nano Banana, etc.) implementiert dieses Interface.
"""

from abc import ABC, abstractmethod
from PIL import Image


class ImageGenerator(ABC):
    """Gemeinsames Interface für alle Bildgeneratoren."""

    @abstractmethod
    def generate(self, prompt: str) -> Image.Image:
        """Generiert ein Bild aus einem Text-Prompt.

        Args:
            prompt: Beschreibung des gewünschten Bildes.

        Returns:
            PIL Image Objekt.
        """
        ...
