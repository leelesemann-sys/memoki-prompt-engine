"""Deck-Generierung und -Verwaltung."""

import random

from game.card import Card


class Deck:
    """Verwaltet ein Set von Memory-Karten.

    Verantwortlich für das Erstellen, Mischen und Anordnen
    der Karten auf dem Spielfeld.
    """

    def __init__(self, cards: list[Card] | None = None):
        self.cards: list[Card] = cards or []

    def shuffle(self) -> None:
        """Mischt die Karten zufällig."""
        random.shuffle(self.cards)

    def add_pair(self, card_a: Card, card_b: Card) -> None:
        """Fügt ein Kartenpaar zum Deck hinzu."""
        self.cards.extend([card_a, card_b])

    @classmethod
    def build_classic(cls, objects: list[str], images: list) -> "Deck":
        """Baut ein Classic-Memory-Deck aus Objekten und Bildern.

        Bei Classic Memory sind beide Karten eines Paares identisch.

        Args:
            objects: Liste von Objekt-Bezeichnungen (z.B. ["cat", "dog"]).
            images: Liste von PIL Images (eins pro Objekt).

        Returns:
            Fertiges, gemischtes Deck.
        """
        deck = cls()
        for i, (obj, img) in enumerate(zip(objects, images)):
            card_a = Card(pair_id=i, label=obj, image=img)
            card_b = Card(pair_id=i, label=obj, image=img)
            deck.add_pair(card_a, card_b)
        deck.shuffle()
        return deck

    @classmethod
    def build_paare(cls, pairs: list[dict], images_a: list, images_b: list) -> "Deck":
        """Baut ein Paare-Memory-Deck: Objekt A ↔ Objekt B.

        Bei Paare-Memory zeigen die Karten zusammengehörige,
        aber verschiedene Objekte (z.B. Topf ↔ Deckel).

        Args:
            pairs: Liste von Dicts mit a_de, b_de, a_en, b_en.
            images_a: Bilder für Objekt A (eins pro Paar).
            images_b: Bilder für Objekt B (eins pro Paar).

        Returns:
            Fertiges, gemischtes Deck.
        """
        deck = cls()
        for i, (pair, img_a, img_b) in enumerate(zip(pairs, images_a, images_b)):
            card_a = Card(pair_id=i, label=pair["a_de"], image=img_a)
            card_b = Card(pair_id=i, label=pair["b_de"], image=img_b)
            deck.add_pair(card_a, card_b)
        deck.shuffle()
        return deck

    @classmethod
    def build_teekesselchen(cls, teekesselchen: list[dict], images_a: list, images_b: list) -> "Deck":
        """Baut ein Teekesselchen-Memory-Deck.

        Bei Teekesselchen zeigen beide Karten verschiedene Bedeutungen
        desselben Wortes (z.B. Bank=Sitzbank ↔ Bank=Geldinstitut).

        Args:
            teekesselchen: Liste von Dicts mit word, label_a, label_b.
            images_a: Bilder für Bedeutung A (eins pro Wort).
            images_b: Bilder für Bedeutung B (eins pro Wort).

        Returns:
            Fertiges, gemischtes Deck.
        """
        deck = cls()
        for i, (tk, img_a, img_b) in enumerate(zip(teekesselchen, images_a, images_b)):
            word = tk["word"]
            card_a = Card(pair_id=i, label=f"{word} ({tk['label_a']})", image=img_a)
            card_b = Card(pair_id=i, label=f"{word} ({tk['label_b']})", image=img_b)
            deck.add_pair(card_a, card_b)
        deck.shuffle()
        return deck

    @classmethod
    def build_mathe_abstrakt(
        cls, numbers: list[int], shape_name: str,
        number_images: list, shape_images: list,
    ) -> "Deck":
        """Baut ein Mathe-Abstrakt-Deck: Zahl ↔ Shapes.

        Args:
            numbers: Liste der Zahlen (z.B. [1, 2, ..., 10]).
            shape_name: Deutscher Shape-Name (z.B. "Kreise").
            number_images: Bilder der Zahlenkarten.
            shape_images: Bilder der Shape-Karten.

        Returns:
            Fertiges, gemischtes Deck.
        """
        deck = cls()
        for i, (num, num_img, shape_img) in enumerate(
            zip(numbers, number_images, shape_images)
        ):
            card_a = Card(pair_id=i, label=f"Zahl {num}", image=num_img)
            card_b = Card(pair_id=i, label=f"{num}x {shape_name}", image=shape_img)
            deck.add_pair(card_a, card_b)
        deck.shuffle()
        return deck

    @classmethod
    def build_mathe_konkret(
        cls, numbers: list[int], objects: list[str],
        number_images: list, object_images: list,
    ) -> "Deck":
        """Baut ein Mathe-Konkret-Deck: Zahl ↔ reale Objekte.

        Jedes Paar hat ein anderes Objekt (z.B. 3 ↔ 3 Tennisbälle, 5 ↔ 5 Äpfel).

        Args:
            numbers: Liste der Zahlen (z.B. [1, 2, ..., 10]).
            objects: Liste der Objekt-Namen (eins pro Zahl).
            number_images: Bilder der Zahlenkarten.
            object_images: Bilder der Objekt-Karten.

        Returns:
            Fertiges, gemischtes Deck.
        """
        deck = cls()
        for i, (num, obj, num_img, obj_img) in enumerate(
            zip(numbers, objects, number_images, object_images)
        ):
            card_a = Card(pair_id=i, label=f"Zahl {num}", image=num_img)
            card_b = Card(pair_id=i, label=f"{num}x {obj}", image=obj_img)
            deck.add_pair(card_a, card_b)
        deck.shuffle()
        return deck
