from poker.deck import Deck
from poker.player import Player

class Game:
    def __init__(self):
        self.deck = Deck()
        self.players = []

    def add_player(self, name):
        self.players.append(Player(name))

    def deal_hole_cards(self):
        self.deck.shuffle()

        for _ in range(2):
            for player in self.players:
                player.hand.append(self.deck.deal())