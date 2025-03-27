import random
from getopt import gnu_getopt


class Card:
    """
    Deck cards with different type of suits and ranks
    """
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    SUITS = ["♣️", "♠️", "♥️", "♦️"]
    def __init__(self, suit, rank):
        """
        Creates objects with suit and rank
        :param suit: suit of the card
        :param rank: rank of the card
        Return 'ValueError' if suit or rank is not in the list 'RANKS' or 'SUITS'
        """
        if rank not in self.RANKS:
            raise ValueError("Invalid Rank")
        if suit not in self.SUITS:
            raise ValueError("Invalid Suit")
        self._suit = suit
        self._rank = rank

    def __eq__(self, other):
        """
        Compare cards to see if they are the same based on their rank
        :param other: new card object
        :return: True if the cards are the same, False if opposit
        """
        return self.rank == other.rank

    def __gt__(self, other):
        """
        Compare cards to see which one has a higher rank
        :param other: new card object
        :return: True if card has higher rank, False if opposit
        """
        return self.RANKS.index(self.rank) > self.RANKS.index(other.rank)

    def __str__(self):
        """
        String representation of the card
        :return: string with [rank, suit]
        """
        return f"{self._rank}{self._suit}"

    def __repr__(self):
        """
        Return the representation of the card
        :return: string card
        """
        return self.__str__()

    @property
    def suit(self):
        """
        Determine the suit of the card
        :return: suit of the card
        """
        return self._suit

    @property
    def rank(self):
        """
        Determine rank of the card
        :return: rank of the card
        """
        return self._rank

class Deck:
    def __init__(self):
        """
        Creates deck of cards with 52 cards
        """
        self._deck = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self._deck.append(Card(suit,rank))

    def __str__(self):
        """
        String representation of the deck
        :return: string with 52 cards
        """
        return str(self._deck)

    def shuffle(self):
        """
        Shuffle the deck randomly
        :return: shuffled deck
        """
        random.shuffle(self._deck)

    def deal(self):
        """
        Remove and return the top card from the deck
        :return: top card from the deck
        """
        return self._deck.pop(0)

if __name__ == "__main__":
    deck = Deck()
    print(deck)
    deck.shuffle()
    print(deck)
    print(deck.deal())
