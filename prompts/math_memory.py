"""Prompt-Builder für Mathe Memory (I und II).

Mathe Memory I (Abstrakt): Karte A zeigt eine Zahl, Karte B zeigt abstrakte Symbole
in der entsprechenden Menge (z.B. 5 Kreise).

Mathe Memory II (Konkret): Karte A zeigt eine Zahl, Karte B zeigt reale Objekte
in der entsprechenden Menge (z.B. 5 Schuhe).
"""

from tools.image import resolve_style, AUDIENCE_MAP


def _layout_hint(n: int) -> str:
    """Gibt eine explizite Anordnungs-Beschreibung zurück, damit die KI die korrekte Anzahl generiert."""
    layouts = {
        1: "a single object centered",
        2: "placed side by side in a single row",
        3: "placed side by side in a single row of 3",
        4: "arranged in 2 rows of 2",
        5: "arranged with 3 in the top row and 2 in the bottom row",
        6: "arranged in 2 rows of 3",
        7: "arranged with 4 in the top row and 3 in the bottom row",
        8: "arranged in 2 rows of 4",
        9: "arranged in 3 rows of 3",
        10: "arranged in 2 rows of 5",
        11: "arranged with 4 in the top row, 4 in the middle row, and 3 in the bottom row",
        12: "arranged in 3 rows of 4",
        13: "arranged with 5 in the top row, 4 in the middle row, and 4 in the bottom row",
        14: "arranged with 5 in the top row, 5 in the middle row, and 4 in the bottom row",
        15: "arranged in 3 rows of 5",
        16: "arranged in 4 rows of 4",
        17: "arranged with 5 in row 1, 4 in row 2, 4 in row 3, and 4 in row 4",
        18: "arranged with 5 in row 1, 5 in row 2, 4 in row 3, and 4 in row 4",
        19: "arranged with 5 in row 1, 5 in row 2, 5 in row 3, and 4 in row 4",
        20: "arranged in 4 rows of 5",
    }
    return layouts.get(n, f"arranged in a neat grid, exactly {n} objects")


def _dice_prompt(n: int) -> str:
    """Baut einen exakten Prompt für Würfelaugen (1-20).

    1-6: Ein einzelner Würfel von oben, klassische Pip-Anordnung.
    7-12: Zwei Würfel nebeneinander.
    13-18: Drei Würfel nebeneinander.
    19-20: Vier Würfel nebeneinander.
    """
    # Standard-Würfelgesichter als klare Beschreibung
    face_desc = {
        1: "showing 1 dot in the center",
        2: "showing 2 dots placed diagonally",
        3: "showing 3 dots placed diagonally from corner to corner",
        4: "showing 4 dots arranged in a 2x2 square pattern, two on top and two on bottom, NO dot in the center",
        5: "showing 5 dots with one in each corner and one in the center",
        6: "showing 6 dots arranged in two columns of 3",
    }

    def _describe_dice(remaining: int) -> list[str]:
        """Zerlegt eine Zahl in Würfel (max 6 pro Würfel) und beschreibt jeden."""
        dice = []
        while remaining > 0:
            val = min(remaining, 6)
            dice.append(face_desc[val])
            remaining -= val
        return dice

    dice_list = _describe_dice(n)

    count_check = f"IMPORTANT: count all black dots – the total must be exactly {n}, not more, not less"

    if len(dice_list) == 1:
        return (
            f"A single white die viewed from directly above, {dice_list[0]}, "
            f"black dots on white surface, the die is large and centered. "
            f"{count_check}"
        )
    else:
        dice_descriptions = " and ".join(
            f"die {i+1} {desc}" for i, desc in enumerate(dice_list)
        )
        return (
            f"Exactly {len(dice_list)} white dice viewed from directly above, side by side, "
            f"{dice_descriptions}, "
            f"black dots on white surfaces, all dice clearly visible and separated. "
            f"{count_check}"
        )


def _tally_prompt(n: int) -> str:
    """Baut einen exakten Prompt für Strichlisten (1-20).

    Klassisches Tally-System:
    - 1-4: einzelne senkrechte Striche
    - 5: vier senkrechte + ein diagonaler Strich
    - 6-20: Gruppen von 5 + Rest
    """
    full_groups = n // 5
    remainder = n % 5

    if n <= 4:
        lines = "one vertical line" if n == 1 else f"{n} vertical lines side by side"
        return (
            f"Tally marks on white background: {lines}, "
            f"drawn in black ink, large and centered. "
            f"IMPORTANT: exactly {n} vertical lines total, no diagonal crossing line"
        )

    parts = []
    if full_groups > 0:
        group_desc = "one group" if full_groups == 1 else f"{full_groups} groups"
        parts.append(
            f"{group_desc} of 5 tally marks (each group = 4 vertical lines "
            f"with 1 diagonal line crossing through them)"
        )
    if remainder > 0:
        line_word = "line" if remainder == 1 else "lines"
        parts.append(f"{remainder} additional vertical {line_word} without crossing")

    layout = " and ".join(parts)
    return (
        f"Tally marks on white background: {layout}, "
        f"drawn in black ink, large and clearly visible, groups well-spaced. "
        f"IMPORTANT: the total count must be exactly {n} marks"
    )


def _domino_prompt(n: int) -> str:
    """Baut einen exakten Prompt für Dominosteine (1-20).

    Ein Dominostein hat zwei Hälften mit je 0-6 Punkten.
    1-12: Ein einzelner Dominostein.
    13-20: Zwei Dominosteine nebeneinander.
    """
    pip_desc = {
        0: "blank (no dots)",
        1: "1 dot in the center",
        2: "2 dots placed diagonally",
        3: "3 dots placed diagonally",
        4: "4 dots in the corners",
        5: "5 dots with 4 in corners and 1 in center",
        6: "6 dots in two columns of 3",
    }

    def _split_for_domino(value: int) -> tuple[int, int]:
        """Teilt eine Zahl möglichst symmetrisch auf zwei Hälften auf (max 6 pro Hälfte)."""
        half_b = min(value, 6)
        half_a = value - half_b
        return half_a, half_b

    count_check = f"IMPORTANT: count all dots – the total must be exactly {n}"

    if n <= 12:
        a, b = _split_for_domino(n)
        return (
            f"A single white domino tile viewed from above, horizontal orientation, "
            f"clearly divided into left half and right half by a center line, "
            f"left half showing {pip_desc[a]}, right half showing {pip_desc[b]}, "
            f"black dots on white surface, the domino is large and centered. "
            f"{count_check}"
        )
    else:
        # Erster Stein: 6|6 = 12, zweiter Stein: Rest
        rest = n - 12
        a2, b2 = _split_for_domino(rest)
        return (
            f"Exactly 2 white domino tiles viewed from above, side by side, horizontal orientation, "
            f"each clearly divided into left and right halves by a center line, "
            f"domino 1: left half showing {pip_desc[6]}, right half showing {pip_desc[6]}, "
            f"domino 2: left half showing {pip_desc[a2]}, right half showing {pip_desc[b2]}, "
            f"black dots on white surfaces, both dominoes clearly visible and separated. "
            f"{count_check}"
        )


def build_number_prompt(
    number: int, style: str = "cartoon", audience: str = "children", theme: str = ""
) -> str:
    """Baut einen Bild-Prompt für eine Zahlenkarte.

    Args:
        number: Die darzustellende Zahl (1-20).
        style: Bildstil-Key (z.B. "cartoon").
        audience: Zielgruppe-Key (z.B. "children").
        theme: Optionales Thema, beeinflusst den Look der Zahl.

    Returns:
        Prompt-String für den Bildgenerator.
    """
    style_desc = resolve_style(style)
    audience_desc = AUDIENCE_MAP.get(audience, AUDIENCE_MAP["children"])

    # Thema beeinflusst nur Farben, NICHT die Form der Ziffer
    if theme:
        theme_hint = (
            f"Use colors and subtle decorative elements inspired by the theme '{theme}', "
            f"but the digit shape itself must remain a clean, standard, clearly readable number. "
            f"Do NOT reshape the number to look like objects from the theme. "
        )
    else:
        theme_hint = "colorful and "

    return (
        f"A single digit showing only the number {number}, displayed very large and bold "
        f"in the center of the image, {theme_hint}clearly readable as a number, "
        f"the digit must have a clean standard shape that is instantly recognizable, "
        f"show the number exactly once, do not duplicate or repeat it, "
        f"high contrast, the number must stand out clearly, "
        f"{style_desc}, {audience_desc}, "
        f"plain white background, bright and clean, no dark backgrounds, "
        f"no borders, no frames, no black edges, "
        f"no other objects, no text except the number. Square format."
    )


def build_shapes_prompt(
    number: int, shape: dict, style: str = "cartoon", audience: str = "children"
) -> str:
    """Baut einen Bild-Prompt für eine Shape-Karte (Mathe Abstrakt).

    Args:
        number: Anzahl der Shapes (1-20).
        shape: Shape-Dict aus math_shapes.json (mit image_prompt_en etc.).
        style: Bildstil-Key.
        audience: Zielgruppe-Key.

    Returns:
        Prompt-String für den Bildgenerator.
    """
    style_desc = resolve_style(style)
    audience_desc = AUDIENCE_MAP.get(audience, AUDIENCE_MAP["children"])

    # Finger brauchen einen speziellen Prompt (Hände statt N einzelne Finger)
    if shape["id"] == "fingers":
        if number <= 5:
            subject = f"A single cartoon hand holding up exactly {number} finger{'s' if number > 1 else ''}, clearly visible"
        else:
            rest = number - 5
            subject = (
                f"Two cartoon hands side by side, the left hand showing all 5 fingers up "
                f"and the right hand showing {rest} finger{'s' if rest > 1 else ''} up, "
                f"{number} fingers total"
            )
        return (
            f"{subject}, high contrast, clearly visible against the background, "
            f"{style_desc}, {audience_desc}, "
            f"plain simple background, no numbers, no text. Square format."
        )

    # Würfelaugen: Standard-Würfel-Anordnungen, ab 7 mehrere Würfel
    if shape["id"] == "dice":
        subject = _dice_prompt(number)
        return (
            f"{subject}, high contrast, clearly visible against the background, "
            f"{style_desc}, {audience_desc}, "
            f"plain white background, no numbers, no text. Square format."
        )

    # Dominosteine: Ein oder zwei Steine mit Punkt-Hälften
    if shape["id"] == "domino":
        subject = _domino_prompt(number)
        return (
            f"{subject}, high contrast, clearly visible against the background, "
            f"{style_desc}, {audience_desc}, "
            f"plain white background, no numbers, no text. Square format."
        )

    # Strichliste: Klassisches Tally-System (4 senkrechte + 1 diagonal = 5)
    if shape["id"] == "tally":
        subject = _tally_prompt(number)
        return (
            f"{subject}, high contrast, clearly visible against the background, "
            f"{style_desc}, {audience_desc}, "
            f"plain white background, no numbers, no text. Square format."
        )

    shape_desc = shape["image_prompt_en"]
    layout = _layout_hint(number)
    return (
        f"Exactly {number} {shape_desc}, {layout}, "
        f"clearly countable, well-spaced, high contrast, vivid colors against the background, "
        f"{style_desc}, {audience_desc}, "
        f"plain simple background, no numbers, no text. Square format."
    )


def build_real_objects_prompt(
    number: int, object_name: str, style: str = "cartoon", audience: str = "children",
    theme: str = "",
) -> str:
    """Baut einen Bild-Prompt für eine Karte mit realen Objekten (Mathe Konkret).

    Args:
        number: Anzahl der Objekte (1-20).
        object_name: Englischer Objekt-Name (z.B. "tennis ball").
        style: Bildstil-Key.
        audience: Zielgruppe-Key.
        theme: Thema-Kontext um Mehrdeutigkeiten aufzulösen.

    Returns:
        Prompt-String für den Bildgenerator.
    """
    style_desc = resolve_style(style)
    audience_desc = AUDIENCE_MAP.get(audience, AUDIENCE_MAP["children"])

    plural = object_name if number == 1 else f"{object_name}s"
    context = f" (in the context of {theme})" if theme else ""
    layout = _layout_hint(number)

    return (
        f"Exactly {number} identical {plural}{context}, nothing else in the image. "
        f"All {number} objects must be the same type of {object_name}{context}, no other objects or items. "
        f"{layout.capitalize()}, clearly countable, well-spaced, "
        f"all objects fully visible and not cropped or cut off at the edges, "
        f"high contrast, vivid colors against the background, "
        f"{style_desc}, {audience_desc}, "
        f"plain simple white background, generous margin around all objects, "
        f"no numbers, no text, no decorations. Square format."
    )
