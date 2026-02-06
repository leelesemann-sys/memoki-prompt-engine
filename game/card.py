"""Card Datenmodell für Memory-Karten."""

from dataclasses import dataclass
from PIL import Image


@dataclass
class Card:
    """Eine einzelne Memory-Karte.

    Attributes:
        pair_id: ID des Kartenpaares (beide Karten eines Paares teilen diese ID).
        label: Beschriftung/Text der Karte (z.B. "5" oder "Katze").
        image: Das generierte Bild (oder None, wenn noch nicht generiert).
        is_revealed: Ob die Karte aktuell aufgedeckt ist.
    """

    pair_id: int
    label: str
    image: Image.Image | None = None
    is_revealed: bool = False
