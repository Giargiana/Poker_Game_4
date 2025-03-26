from deck import Deck, Card

class PokerHand:
    def __init__(self, deck):

        cards = []
        for i in range(5):
            cards.append(deck.deal())
        self._cards = cards

    @property
    def cards(self):
        return self._cards

    def __str__(self):
        return str(self.cards)

    @property
    def is_flush(self):
        for card in self.cards[1:]:
            if self.cards[0].suit != card.suit:
                return False
        return True

    @property
    def is_full_house(self):
        return self.num_match == 8

    @property
    def num_match(self):
        matches = 0
        for i in range(len(self.cards)):
            for j in range(len(self.cards)):
                if i == j:
                    continue
                if self.cards[i].rank == self.cards[j].rank:
                    matches += 1
        return matches

    @property
    def is_pair(self):
        if self.num_match == 2: # simpler
            return True
        return False

    @property
    def is_two_pair(self):
        return self.num_match == 4 # advanced

    @property
    def is_tris(self):
        return self.num_match == 6 # advanced

    @property
    def is_quad(self):
        return self.num_match == 12 # advanced

    @property
    def is_straight(self):
        self.cards.sort()
        distance = Card.RANKS.index(self.cards[4].rank) - \
                   Card.RANKS.index(self.cards[0].rank)
        return self.num_match == 0 and distance == 4

count = 0
matches = 0
while matches < 1000:
    deck = Deck()
    deck.shuffle()
    hand = PokerHand(deck)

    if hand.is_straight:
        matches += 1
        print(hand)
    count += 1

print(f"probability of a straight is {100*matches/count}%")