"""Prompt-Builder für Paare Memory.

Modus: Zusammengehörige Objekte bilden ein Paar
(z.B. Topf & Deckel, Kugelschreiber & Notizblock).
Karte A zeigt Objekt A, Karte B zeigt Objekt B.
"""

from tools.image import resolve_style, AUDIENCE_MAP


def build_pair_object_prompt(
    object_name_en: str, style: str = "cartoon", audience: str = "children"
) -> str:
    """Baut einen Bild-Prompt für ein einzelnes Objekt im Paare-Modus.

    Args:
        object_name_en: Englischer Objekt-Name (z.B. "cooking pot").
        style: Bildstil-Key.
        audience: Zielgruppe-Key.

    Returns:
        Prompt-String für den Bildgenerator.
    """
    style_desc = resolve_style(style)
    audience_desc = AUDIENCE_MAP.get(audience, AUDIENCE_MAP["children"])

    return (
        f"A single realistic {object_name_en}, showing the actual real-world object, "
        f"the object must keep its normal real shape – "
        f"do NOT reshape it into an animal, whale, duck, character, or toy, "
        f"do NOT add faces, eyes, or animal features to the object, "
        f"clearly recognizable and centered, "
        f"high contrast, the object must stand out clearly against the background, "
        f"{style_desc}, {audience_desc}, "
        f"plain white background, bright and clean, "
        f"no other objects, no text. Square format."
    )
