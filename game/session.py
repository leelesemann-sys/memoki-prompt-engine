"""Spielzustand-Verwaltung (GameSession)."""

from game.deck import Deck


class GameSession:
    """Verwaltet den Zustand einer laufenden Spielrunde.

    Attributes:
        deck: Das aktuelle Kartendeck.
        moves: Anzahl bisheriger Züge.
        pairs_found: Anzahl gefundener Paare.
        is_finished: Ob das Spiel beendet ist.
    """

    def __init__(self, deck: Deck):
        self.deck = deck
        self.moves: int = 0
        self.pairs_found: int = 0
        self.is_finished: bool = False
