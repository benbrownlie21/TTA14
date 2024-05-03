import random


class Card:
    def __init__(self):
        self.suit = ("Hearts", "Diamonds", "Clubs", "Spades")
        self.value = ("Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King")


class Deck(Card):
    def shuffle(self):
        self.card_deck = []
        for s in self.suit:
            for v in self.value:
                self.card_deck.append(f"{v} of {s}")
        random.shuffle(self.card_deck)
        print(self.card_deck)

    def deal(self):
        delt_card = random.choice(self.card_deck)
        print(f"\nDelt Card: {delt_card}")
        self.card_deck.remove(delt_card)
        print(f"\nRemaining Cards: {self.card_deck}")


deck = Deck()
deck.shuffle()
deck.deal()
