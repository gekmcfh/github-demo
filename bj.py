import cards,games

class BJCard (cards.Card):
    """Black jack card"""
    ACE_VALUE=1
    @property
    def value(self):
        if self.is_face_up:
            v = BJCard.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
            else:
                v = None
            return v


class BJDeck (cards.Deck):
    """Black jack deck"""
    def populate(self):
        for suit in BJCard.SUITS:
            for rank in BJCard.RANKS:
                self.cards.append(BJCard(rank,suit))


class BJHand(cards.Hand):
    """a 'Hand' - player's cards set"""
    def __init__(self, name):
        super(BJHand, self).__init__()
        self.name = name

    def __str__(self):
        rep = self.name + ":\t" + super(BJHand, self).__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"

    @property
    def total(self):
        #if one of cards value equals None, then property equals None
        for card in self.cards:
            if not card.value:
                return None
        #getting values sum, ACE is one point
        t = 0
        for card in self.cards:
            t += card.value
        #determine whether player hand contains ACE
        contains_ace = False
        for card in self.cards:
                if card.value is BJCard.ACE_VALUE:
                    contains_ace = True
        # if ACE is on a hands and point sum less or equals 11, then ACE is 11 points
        if contains_ace and t <= 11:
            t+=10
        return t
