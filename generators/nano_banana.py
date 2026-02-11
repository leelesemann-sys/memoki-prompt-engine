"""Google Nano Banana Pro (Gemini) Bildgenerator."""

import io
from PIL import Image
from google import genai
from google.genai import types

from config.settings import GOOGLE_API_KEY, GOOGLE_IMAGE_MODEL
from generators.base import ImageGenerator


class NanoBananaGenerator(ImageGenerator):
    """Generiert Bilder über Google AI Studio (Gemini).

    Nutzt Gemini's native Bildgenerierung über generate_content
    mit response_modalities=["IMAGE"].
    """

    def __init__(self):
        self.client = genai.Client(api_key=GOOGLE_API_KEY)
        self.model = GOOGLE_IMAGE_MODEL

    def generate(self, prompt: str) -> Image.Image:
        """Generiert ein Bild mit Gemini (Nano Banana Pro).

        Args:
            prompt: Beschreibung des gewünschten Bildes.

        Returns:
            PIL Image Objekt.
        """
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_modalities=["IMAGE"],
            ),
        )

        # Bild aus der Response extrahieren
        for part in response.candidates[0].content.parts:
            if part.inline_data and part.inline_data.mime_type.startswith("image/"):
                return Image.open(io.BytesIO(part.inline_data.data))

        raise RuntimeError("Gemini hat kein Bild in der Antwort zurückgegeben")
