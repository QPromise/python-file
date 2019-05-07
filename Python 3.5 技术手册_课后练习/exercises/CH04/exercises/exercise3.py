from random import randint
from functools import reduce

class Card:
    def __init__(self, suit, symbol):
        self.suit = suit
        self.symbol = symbol

    def __str__(self):
        return self.suit + self.symbol

class Poker:
    cards = [Card(
        {0: "桃", 1: "心", 2: "磚", 3: "梅"}[i // 13],
        {0: "K ", 1: "A ", 11: "J ", 12: "Q "}.get(
            (i + 1) % 13, "%-2d" % ((i + 1) % 13))
    ) for i in range(52)]

    @staticmethod
    def shuffle():
        def swap(cards, i, j):
            a, b = sorted([i, j])
            return cards if a == b else (cards[0:a] + [cards[b]] +
                       cards[a + 1:b] + [cards[a]] + cards[b + 1:])
        return reduce(lambda cards, i: swap(cards, i, randint(0, 51)),
                   range(len(Poker.cards)), Poker.cards)

cards = Poker.shuffle()
for i in range(len(cards)):
    print(cards[i], end = "\n" if (i + 1) % 13 == 0 else " ")