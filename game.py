import numpy as np
import random

class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit # Hearts, Spades, Diamonds, Clubs
        self.rank = rank # 2-10, Jack, Queen, King, Ace
        self.value = value # Ace is one, face cards are 10, rest are face value
    def get_suit(self):
        return self.suit
    def get_rank(self):
        return self.rank
    def name(self):
        print(f"{self.rank} of {self.suit}")

class Deck:
    def __init__(self):
        
        deck = [] # building the deck
        suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
        ranks = {"Ace":1, "Two":2, "Three":3, "Four":4, "Five":5, 
                 "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, 
                 "Jack":10, "Queen":10, "King":10}
        for suit in suits:
            for rank, value in ranks.items():
                deck.append(Card(suit, rank, value))
        
        self.cards = deck # normal 52 deck of playing cards

    def random_draw(self):
        choice = random.choice(self.cards)
        self.cards.remove(choice)
        return choice

class Hand:
    def __init__(self, player): # player: 1, 2 (maybe will add 3 players)
        self.cards = [] 
    
class PlayerHand(Hand): # draw 6 cards, then discard 2 into crib
    def __init__(self, player):
        super().__init__(player)
    def draw_card(self, card: Card): 
        if len(self.cards) < 6:
            self.cards.append(card)
            return True
        return False
    def discard_card(self, card: Card):
        if card in self.cards and len(self.cards) > 4:
            self.cards.remove(card)
            return card
        return False

class Crib(Hand): # points in crib alternate between players
    def __init__(self, player):
        super().__init__(player)
    def add_card(self, card: Card):
        if len(self.cards) < 4:
            self.cards.append(card)
            return True
        return False



