"""Deck-Generierung und -Verwaltung."""

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
        import random
        random.shuffle(self.cards)

    def add_pair(self, card_a: Card, card_b: Card) -> None:
        """Fügt ein Kartenpaar zum Deck hinzu."""
        self.cards.extend([card_a, card_b])
