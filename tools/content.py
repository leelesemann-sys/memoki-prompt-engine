"""Content-Generierung – erzeugt Objekt-Listen per LLM + lädt Teekesselchen.

Nutzt Gemini 2.5 Flash, um thematisch passende Objekte
für Memory-Karten zu generieren (Classic, Mathe Konkret).
Lädt Teekesselchen aus der JSON-Wissensbasis.
"""

import json
import random
from pathlib import Path
from google import genai
from google.genai import types

from config.settings import GOOGLE_API_KEY, GOOGLE_CHAT_MODEL

KNOWLEDGE_DIR = Path(__file__).resolve().parent.parent / "knowledge"

GENERATE_OBJECTS_PROMPT = """\
Du generierst eine Liste von Objekten, die sich gut als Bild darstellen lassen.

AUFGABE:
Generiere {count} verschiedene, konkrete Objekte zum Thema "{theme}".
Die Objekte sollen für {audience} geeignet sein.

ANFORDERUNGEN:
- Objekte müssen visuell klar unterscheidbar sein
- Objekte müssen als {style} darstellbar sein
- Jedes Objekt nur einmal verwenden
- Keine abstrakten Konzepte

GUTE BEISPIELE:

Thema: "Tiere", Zielgruppe: "Kinder"
→ ["cat", "elephant", "fish", "rabbit", "butterfly", "dog", "horse", "bird", "frog", "turtle"]

Thema: "Essen", Zielgruppe: "Erwachsene"
→ ["apple", "croissant", "sushi roll", "pizza slice", "cupcake", "pretzel", "taco", "donut", "grape bunch", "cheese wheel"]

SCHLECHTE BEISPIELE (vermeide):
- "love", "happiness" ← abstrakt
- "water", "sand" ← Masse, nicht einzeln darstellbar
- "car" und "automobile" ← Synonyme

WICHTIG: Alle Objekt-Namen MÜSSEN auf ENGLISCH sein (für Bild-Prompts).

AUSGABE:
Antworte NUR mit einem JSON-Array von englischen Strings, keine Erklärung.
["object1", "object2", ...]
"""


def generate_objects(
    theme: str,
    count: int,
    audience: str = "children",
    style: str = "cartoon",
) -> list[str]:
    """Generiert eine Liste von Objekten per LLM.

    Args:
        theme: Thema (z.B. "Tiere", "Fahrzeuge").
        count: Anzahl gewünschter Objekte.
        audience: Zielgruppe ("children", "teenagers", "adults").
        style: Bildstil ("cartoon", "photorealistic", etc.).

    Returns:
        Liste von englischen Objekt-Bezeichnungen.
    """
    client = genai.Client(api_key=GOOGLE_API_KEY)

    prompt = GENERATE_OBJECTS_PROMPT.format(
        count=count,
        theme=theme,
        audience=audience,
        style=style,
    )

    response = client.models.generate_content(
        model=GOOGLE_CHAT_MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.8,
        ),
    )

    text = response.text.strip()

    # JSON aus Markdown-Block extrahieren falls nötig
    if "```" in text:
        start = text.index("[")
        end = text.rindex("]") + 1
        text = text[start:end]

    objects = json.loads(text)

    if not isinstance(objects, list) or len(objects) < count:
        raise ValueError(f"Erwartet {count} Objekte, bekommen: {len(objects)}")

    return objects[:count]


GENERATE_COUNTABLE_OBJECTS_PROMPT = """\
Du generierst eine Liste von ZÄHLBAREN Objekten für ein Mathe-Memory-Spiel.
Die Karten zeigen eine Zahl (1–{count}) neben dem entsprechenden Bild mit genau so vielen Objekten.

AUFGABE:
Generiere {count} verschiedene, zählbare Objekte zum Thema "{theme}".
Die Objekte sollen für {audience} geeignet sein.

HARTE ANFORDERUNGEN:
- Objekte MÜSSEN diskret und einzeln zählbar sein (man kann sie mit dem Finger abzählen)
- Objekte MÜSSEN klein genug sein, dass 1 bis 10 Stück auf ein Bild passen
- Jedes Objekt nur einmal verwenden
- Objekte MÜSSEN visuell klar unterscheidbar sein
- Objekte MÜSSEN eindeutig zum Thema passen und sofort als Teil des Themas erkennbar sein
- WICHTIGSTE REGEL: Zeige die Sache SELBST, nicht Zutaten, Zubehör oder Teile davon!
  Wenn das Thema "Schuhe" ist → verschiedene Schuhtypen (sneaker, boot, sandal, high heel)
  NICHT Schuh-Zubehör (shoe buckle, shoe eyelet, shoe charm, shoelace)
  Wenn das Thema "Getränke" ist → verschiedene Getränke IM GLAS/BECHER (beer glass, coffee cup, wine glass, juice box, soda can, smoothie cup)
  NICHT Zutaten oder Zubehör (coffee bean, tea bag, ice cube, lemon slice, sugar cube)
- Jedes Objekt muss auf einem Bild sofort erkennbar sein, auch für Kinder
- Vermeide mehrdeutige Wörter (z.B. "button" kann Knopf oder Taste sein)
- Benutze spezifische, eindeutige Bezeichnungen (z.B. "USB flash drive" statt "drive")

GUTE BEISPIELE (zählbar + klein + sofort erkennbar):
Thema "Sport" → ["tennis ball", "soccer ball", "badminton shuttlecock", "ice skate", "boxing glove"]
Thema "Essen" → ["apple", "cupcake", "pretzel", "cookie", "cherry"]
Thema "Tiere" → ["ladybug", "goldfish", "butterfly", "snail", "duckling"]
Thema "Technik" → ["USB flash drive", "computer mouse", "battery", "light bulb", "gear wheel"]
Thema "Schuhe" → ["sneaker", "rain boot", "sandal", "high heel shoe", "hiking boot", "ballet flat", "flip flop", "cowboy boot"]
Thema "Getränke" → ["beer glass", "coffee cup", "wine glass", "juice box", "soda can", "smoothie cup", "tea cup", "cocktail glass"]

SCHLECHTE BEISPIELE (VERMEIDE!):
- "Fußballfeld", "Skipiste", "Schwimmbad" ← zu groß, nicht zählbar
- "Himmel", "Wasser", "Sand" ← Masse, nicht diskret
- "Mannschaft", "Rennen" ← abstrakt/Ereignis
- "Elefant", "Giraffe" ← zu groß für 10 Stück auf einem Bild
- "button", "key", "chip" ← mehrdeutig, passt zu mehreren Themen
- "shoe buckle", "shoe eyelet", "shoe charm" ← Zubehör statt die Sache selbst
- "coffee bean", "tea bag", "ice cube", "lemon slice" ← Zutaten statt das Getränk selbst

WICHTIG: Alle Objekt-Namen MÜSSEN auf ENGLISCH sein.

AUSGABE:
Antworte NUR mit einem JSON-Array von englischen Strings, keine Erklärung.
["object1", "object2", ...]
"""


def generate_countable_objects(
    theme: str,
    count: int,
    audience: str = "children",
) -> list[str]:
    """Generiert zählbare Objekte per LLM für Mathe Memory II.

    Args:
        theme: Thema (z.B. "Sport", "Essen").
        count: Anzahl verschiedener Objekte.
        audience: Zielgruppe.

    Returns:
        Liste von englischen Objekt-Bezeichnungen.
    """
    client = genai.Client(api_key=GOOGLE_API_KEY)

    prompt = GENERATE_COUNTABLE_OBJECTS_PROMPT.format(
        count=count,
        theme=theme,
        audience=audience,
    )

    response = client.models.generate_content(
        model=GOOGLE_CHAT_MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.8,
        ),
    )

    text = response.text.strip()

    if "```" in text:
        start = text.index("[")
        end = text.rindex("]") + 1
        text = text[start:end]

    objects = json.loads(text)

    if not isinstance(objects, list) or len(objects) < count:
        raise ValueError(f"Erwartet {count} Objekte, bekommen: {len(objects)}")

    return objects[:count]


def load_math_shape(shape_id: str) -> dict:
    """Lädt eine Shape-Definition für Mathe Abstrakt.

    Args:
        shape_id: Shape-Kennung (z.B. "circles", "stars", "surprise").

    Returns:
        Dict mit id, name_de, name_en, image_prompt_en, etc.
    """
    path = KNOWLEDGE_DIR / "math_shapes.json"
    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    if shape_id == "surprise":
        pool = data["surprise_pool"]
        shape_id = random.choice(pool)

    for category in data["shape_categories"].values():
        for shape in category["shapes"]:
            if shape["id"] == shape_id:
                return shape

    raise ValueError(f"Shape '{shape_id}' nicht gefunden")


def load_pairs(theme: str, count: int, lang: str = "de") -> list[dict]:
    """Lädt zusammengehörige Objektpaare aus der Wissensbasis.

    Args:
        theme: Thema-Key (z.B. "küche", "sport", "tiere").
        count: Anzahl gewünschter Paare.
        lang: Sprache für Display-Labels ("de" oder "en").

    Returns:
        Liste von Dicts:
        [{"a_en": "cooking pot", "b_en": "pot lid", "a_label": "Topf", "b_label": "Deckel"}]
    """
    path = KNOWLEDGE_DIR / "pairs_v2.json"
    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    themes = data["themes"]

    # Thema suchen (case-insensitive, Deutsch oder Englisch)
    theme_lower = theme.lower()
    theme_data = None
    for key, val in themes.items():
        if (key.lower() == theme_lower
                or val["name_de"].lower() == theme_lower
                or val["name_en"].lower() == theme_lower):
            theme_data = val
            break

    if theme_data is None:
        available = [v[f"name_{lang}"] for v in themes.values()]
        raise ValueError(
            f"Thema '{theme}' nicht gefunden. Verfügbar: {', '.join(available)}"
        )

    pairs = theme_data["pairs"]
    selected = random.sample(pairs, min(count, len(pairs)))

    label_key = lang if lang in ("de", "en") else "de"
    return [
        {
            "a_en": p["a"]["en"],
            "b_en": p["b"]["en"],
            "a_label": p["a"][label_key],
            "b_label": p["b"][label_key],
        }
        for p in selected
    ]


def load_pairs_themes(lang: str = "de") -> list[str]:
    """Gibt alle verfügbaren Paare-Themen zurück."""
    path = KNOWLEDGE_DIR / "pairs_v2.json"
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    name_key = f"name_{lang}" if lang in ("de", "en") else "name_de"
    return [v[name_key] for v in data["themes"].values()]


def load_teekesselchen(count: int, lang: str = "de") -> list[dict]:
    """Lädt zufällige Teekesselchen aus der JSON-Wissensbasis.

    Args:
        count: Anzahl gewünschter Teekesselchen-Paare.
        lang: Sprache für Display-Labels ("de" oder "en").

    Returns:
        Liste von Dicts mit Struktur:
        [{"word": "Bank", "meaning_a": "wooden park bench...", "meaning_b": "bank building..."}]
    """
    path = KNOWLEDGE_DIR / "teekesselchen_v2.json"
    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    entries = data["entries"]
    selected = random.sample(entries, min(count, len(entries)))

    label_key = lang if lang in ("de", "en") else "de"
    return [
        {
            "word": e["word"],
            "meaning_a": e["meaning_a"]["en"],
            "meaning_b": e["meaning_b"]["en"],
            "label_a": e["meaning_a"][label_key],
            "label_b": e["meaning_b"][label_key],
        }
        for e in selected
    ]
