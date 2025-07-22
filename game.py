import numpy as np
import random
import itertools

class Card:
    def __init__(self, suit, rank, value, sort_value):
        self.suit = suit # Hearts, Spades, Diamonds, Clubs
        self.rank = rank # 2-10, Jack, Queen, King, Ace
        self.value = value # Ace is one, face cards are 10, rest are face value
        self.sort_value = sort_value # same as value except for face cards
        self.starter:bool = False
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
        ranks = {"Ace":[1,1], "Two":[2,2], "Three":[3,3], "Four":[4,4], "Five":[5,5], 
                 "Six":[6,6], "Seven":[7,7], "Eight":[8,8], "Nine":[9,9], "Ten":[10,10], 
                 "Jack":[10,11], "Queen":[10,12], "King":[10,13]}
        for suit in suits:
            for rank, value in ranks.items():
                deck.append(Card(suit, rank, value[0], value[1]))
        
        self.cards = deck # normal 52 deck of playing cards

    def random_draw(self):
        choice = random.choice(self.cards)
        self.cards.remove(choice)
        return choice
    def flip_starter(self):
        choice = random.choice(self.cards)
        choice.starter = True
        self.cards.remove(choice)
        return choice

# ways to score hands in cribbage (score):
# add value of multiple cards to 15 (2)
# pairs (2)
# runs of three or more (# of cards in run)
# flushes in hand (4, 5 if starter card is same suit as hand, flush crib must include starter card)
# nobs: suit of jack in hand matches starter card(1)


class Hand:
    def __init__(self, player): # player: 1, 2 (maybe will add 3 players)
        self.cards = [] 
        self.score = 0
        self._saved_runs = []
    
    def _score_five(self):
        # check runs
        suit = None
        starter_suit = None
        sum_values = 0
        run = []
        for i, card in enumerate(self.cards):
            if i == 0 or (i == 1 and run[0] + 1 == card.value) or (i > 1 and run and run[len(run)-1] + 1 == card.value):
                run.append(card.value)
            else:
                run = []
            sum_values += card.value
            if card.starter:
                starter_suit = card.suit
            if suit != card.suit and card.starter is False:
                suit = None
            if (i == 4 and suit) or (i == 3 and suit and starter_suit == None): # flush reached on fourth card without starter or fifth card 
                self.score += 4
            if i == 4 and suit and starter_suit == suit:
                self.score += 1
            if i == 4 and sum_values == 15: # five cards add to 15
                self.score += 2
            
            
            




        
    # def _score_four(self, saved_runs):
    # def _score_three(self, saved_runs):
    # def _score_two(self, saved_runs):
    # def score_hand(self):
    #     self.cards = sorted(self.cards, key=lambda v: v.sort_value, reverse=True)
        
        
        
    #     _score_five()
    #     _score_four()
    #     _score_three()
    #     _score_two()
            
        # score all unique subsets of size 2 (check for 15's and pairs, nobs if one of pair is starter and the other is Jack with same suit)
        # score all unique subsets of size 3 (check for 15's and runs)
        # score all unique subsets of size 4 (check for 15's, runs, and flushes)
        #   Can't double count runs (ex: 2, 3, 4 and 2, 3, 4, 5 counted as seperate runs), flushes at this level cannot contain starter
        # score full hand of 5 (check for 15's, runs (without double counting), flushes)
        
    




    
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
    def add_card(self, card: Card): # take discard_card of player hand as argument
        if len(self.cards) < 4:
            self.cards.append(card)
            return True
        return False

# hands to test:
# 
d = Deck()
hand = []
print(bool(hand and hand[1]))
# for i in [1, 2, 3, 4, 5]:
#     card = d.random_draw()
#     hand.append(card)
# hand = sorted(hand, key=lambda v: v.sort_value, reverse=True)
# [card.name() for card in hand]