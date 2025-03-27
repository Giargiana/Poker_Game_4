from getopt import gnu_getopt

from deck import Deck, Card

class PokerHand:
    """
    A class that represents a poker hand, therefore 5 cards drawn from the deck. Evaluates different poker hands and 'points'.
    Starting from pair, two pairs, tris, straight, flush, full house, poker, color flush and royal flush
    """
    def __init__(self, deck):
        """
        Creates a PokerHand by drawing 5 random cards from the previous given random deck of 52 cards
        :param deck:
        """
        cards = []
        for i in range(5):
            cards.append(deck.deal())
        self._cards = cards

    @property
    def cards(self):
        """
        Get a list of 5 cards in the hand
        :return: five cards
        """
        return self._cards

    def __str__(self):
        """
        Return as output a string representation of the poker hand
        :return: string containing 5 cards
        """
        return str(self.cards)

    @property
    def is_flush(self):
        """
        Check if the hand is a flush, so if all cards have the same suit. It compares the suit of all cards with the first card's suit.
        Compares the suit of the first card (self.cards[0].suit) with the suit of each of the other cards (self.cards[1:])
        :return: True if they have same suit, False otherwise
        """
        for card in self.cards[1:]:
            if self.cards[0].suit != card.suit:
                return False
        return True

    @property
    def is_full_house(self):
        """
        Check if the hand is a full house, consists of a tris and a pair.
        The num_match property returns the total number of rank matches in the hand. A full house has exactly 8 rank matches (three matches for one rank and two matches for another)
        :return: True if full house, False if opposite
        """
        return self.num_match == 8

    @property
    def num_match(self):
        """
        Counts the number of matching cards in the given hand drawn randomly. It is done by comparing cards with every other card in the hand
        Determines various hands type like pairs, tris, and a full house
        :return: total number of matches
        """
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
        """
        Checks if the hand has a single pair. 'num_match' property is used here to count the number of rank matches
        :return: True if the hand has one pair, False if opposite
        """
        if self.num_match == 2: # simpler
            return True
        return False

    @property
    def is_two_pair(self):
        """
        Check if the hand contains two pairs. It consists of two different ranks, each with two cards. If num_match = 4 then there are two pairs
        :return: True if the hand has two pairs, otherwise False.
        """
        return self.num_match == 4 # advanced

    @property
    def is_tris(self):
        """
        Check if the hand contains three cards of the same rank. If num_match = 6 then there is a tris
        :return: True if the hand is a three-of-a-kind, otherwise False.
        """
        return self.num_match == 6 # advanced

    @property
    def is_quad(self):
        """
        Check if the hand contains four cards of the same rank. If num_match = 12 then there is a quad
        :return: True if the hand is a four-of-a-kind, otherwise False.
        """
        return self.num_match == 12 # advanced

    @property
    def is_straight(self):
        """
        Check if the hand is a straight (five consecutive ranks).
        The hand is sorted, and the difference between the highest and lowest rank is checked. The distance between the lowest and highest cards
        in the sorted hand is calculated by comparing their positions in the Card.RANKS list.
        If the distance between the highest and lowest ranks is 4, and there are no matching ranks (num_match == 0), the hand is a straight.
        :return: True if the hand is a straight, otherwise False.
        """
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
