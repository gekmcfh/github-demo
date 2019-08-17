#Playing Cards
#Demonstrates combining objects

class Card(object):
    """A playing card."""
    RANKS = ["A","2","3","4","5","6","7",
             "8","9","10","J","Q","K"]
    SUITS = ["c","d","h","s"]

    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep


class Hand(object):
    """A hand of playing cards."""
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + " "
        else:
            rep =  "<empty>"
        return rep

    def clear(self):
        self.cards=[]

    def add(self,card):
        self.cards.append(card)

    def give(self,card,other_hand):
        self.cards.remove(card)
        other_hand.add(card)

class Deck(Hand):
    """A hand of playing cards."""

    def populate(self):
        self.cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank,suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal (self,hands,per_hand = 1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card=self.cards[0]
                    self.give(top_card,hand)
                else:
                    print("Cannot continue deal! Out of cards.")


class Unprintable_Card(Card):
    """A card, that won't reveal its rank or suit when printed."""
    def __str__(self):
        return "<unprintable>"


class Positionable_Card(Card):
    """A card that can be face up or face down."""
    def __init__(self,rank,suit,face_up=True):
        super(Positionable_Card,self).__init__(rank,suit)
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            rep = super(Positionable_Card,self).__str__()
        else:
            rep = "XX"
        return rep

    def flip(self):
        self.is_face_up = not self.is_face_up


#main
card1 = Card("A","c")
card2 = Unprintable_Card("A","d")
card3 = Positionable_Card("A","h")

print("Печатаю объект Card:")
print(card1)
print("Печатаю объект Unprintable_Card:")
print(card2)
print("Печатаю объект Positionable_Card:")
print(card3)
print("переворачиваю объект Positionable_Card:")
card3.flip()
print(card3)
