import random

suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]


class Deck:
    def __init__(self):
        self.cards = []

        for rank in ranks:
            for suit in suits:
                self.cards.append((rank, suit))
