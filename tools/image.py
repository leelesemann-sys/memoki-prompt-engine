"""Bild-Tools – Prompt-Builder und Image-Generierung.

Baut Memory-Karten-Prompts und generiert Bilder
über Gemini 3 Pro (Standard) oder Gemini 2.5 Flash (Fallback).
"""

import io
from PIL import Image
from google import genai
from google.genai import types

from config.settings import GOOGLE_API_KEY, GOOGLE_IMAGE_MODEL, GOOGLE_IMAGE_MODEL_FAST

# Stil-Mapping (deutsch → englisch Prompt-Fragmente)
STYLE_MAP = {
    "cartoon": "cartoon illustration style, bold outlines, vibrant colors, the object must remain clearly recognizable",
    "photorealistic": "photorealistic, high detail, professional photography, soft studio lighting",
    "watercolor": "watercolor painting style, soft edges, pastel colors, the object must remain clearly recognizable",
    "minimalist": "minimalist flat design, simple shapes, limited color palette",
    "artistic": "painterly illustration, soft brushstrokes, the object must remain clearly recognizable",
    "black-and-white": "black and white only, grayscale, no color, monochrome, pencil sketch style",
    "pencil": "pencil drawing, hand-sketched, graphite on paper, black and white, no color",
    "retro": "retro vintage illustration, muted warm tones, 1970s aesthetic",
    "pixel": "pixel art style, 8-bit retro game aesthetic, blocky shapes",
    "comic": "comic book illustration, bold ink outlines, halftone dots",
}


def resolve_style(style: str) -> str:
    """Löst einen Stil-Key auf: bekannte Keys → STYLE_MAP, sonst Freitext durchreichen."""
    return STYLE_MAP.get(style, style)


# Zielgruppen-Anpassung
AUDIENCE_MAP = {
    "children": "bright cheerful colors, friendly appearance, suitable for children",
    "teenagers": "cool modern aesthetic, trendy colors",
    "adults": "sophisticated, elegant, refined details",
}


def build_image_prompt(subject: str, style: str = "cartoon", audience: str = "children") -> str:
    """Baut einen optimierten Bild-Prompt für eine Memory-Karte.

    Args:
        subject: Das darzustellende Motiv (englisch, z.B. "elephant").
        style: Bildstil-Schlüssel (cartoon, photorealistic, etc.).
        audience: Zielgruppe (children, teenagers, adults).

    Returns:
        Fertiger Prompt-String für den Bildgenerator.
    """
    style_desc = resolve_style(style)
    audience_desc = AUDIENCE_MAP.get(audience, AUDIENCE_MAP["children"])

    prompt = (
        f"A {subject}, {style_desc}, {audience_desc}. "
        f"High contrast, ensure the subject stands out clearly against the background. "
        f"Centered on pure white background. No text. Square format."
    )
    return prompt


def generate_card_image(prompt: str, use_fast: bool = False) -> Image.Image:
    """Generiert ein Kartenbild über Gemini.

    Args:
        prompt: Der Bild-Prompt.
        use_fast: True = Gemini 2.5 Flash (schnell/günstig), False = Gemini 3 Pro (Qualität).

    Returns:
        PIL Image Objekt.
    """
    client = genai.Client(api_key=GOOGLE_API_KEY)
    model = GOOGLE_IMAGE_MODEL_FAST if use_fast else GOOGLE_IMAGE_MODEL

    response = client.models.generate_content(
        model=model,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_modalities=["IMAGE"],
        ),
    )

    for part in response.candidates[0].content.parts:
        if part.inline_data and part.inline_data.mime_type.startswith("image/"):
            return Image.open(io.BytesIO(part.inline_data.data))

    raise RuntimeError(f"Kein Bild in Gemini-Antwort ({model})")
