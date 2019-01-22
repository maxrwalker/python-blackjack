"""

Card game methods to support Blackjack implementation.
Author: Max Walker

"""

import random


# Creates a single deck of card
def make_deck():
    card_idx = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
    deck = []
    for suit in suits:
        for val in card_idx:
            deck.append((val, suit))
    return deck


# Shuffles a deck of card
def shuffle_deck(deck, cuts):
    # just cut the deck (n) times:
    for cut_count in range(cuts):
        cut_point = random.randint(0, 51)
        top_slice = deck[cut_point:52]
        bottom_slice = deck[0: cut_point]
        deck = bottom_slice
        for slice_card in top_slice:
            deck.insert(0, slice_card)
    return deck


# Gets the name of a card tuple
def get_card_name(card):
    name = str(card[0])
    if card[0] == 1:
        name = "Ace"
    elif card[0] == 11:
        name = "Jack"
    elif card[0] == 12:
        name = "Queen"
    elif card[0] == 13:
        name = "King"

    return name + " of " + card[1]


# Get text describing the cards in this hand
def get_hand_text(hand_name, hand):
    text = hand_name + ":"
    for card in hand:
        text += "[" + get_card_name(card) + "] "
    return text
