"""

Non-Object-Oriented Blackjack
Author: Max Walker

This is an attempt to learn Python by implementing Blackjack using
a functional / non-OO implementation only.

This is my first Python program, please excuse any Python coding
convention faux pas!

"""

import cardgames
import time

LINE = "---------------------------"


# Get the value of hand, specifying is Ace counts as 1 or 11
def hand_sum(hand, ace_eleven):
    return_sum = 0
    for card in hand:
        card_val = card[0]
        if card_val == 1 and ace_eleven:
            card_val = 11
        elif card_val > 10:
            card_val = 10
        return_sum += card_val
    return return_sum


# Return true if the hand is bust
def is_bust(hand):
    return hand_sum(hand, False) > 21


# Return true if the dealer should stand (17 or higher(
def is_dealer_stand_hand(hand):
    if 17 <= hand_sum(hand, True) <= 21:
        return True
    else:
        return hand_sum(hand, False) >= 17


# Play a hand of Blackjack. New shuffled deck used for each game.
def play_blackjack():
    # Shuffle deck of cards
    deck = cardgames.make_deck()
    deck = cardgames.shuffle_deck(deck, 300)

    # Deal 2 cards each to dealer and player, players sees 1 of dealers cards:
    players_hand = [deck.pop()]
    dealers_hand = [deck.pop()]
    players_hand.append(deck.pop())
    dealers_hand.append(deck.pop())
    print("Dealers Hand: [Face Down] [" + cardgames.get_card_name(dealers_hand[1]) + "]")
    print(cardgames.get_hand_text("Players", players_hand))
    player_move = ""
    bust = False

    # Player play phase:
    while player_move != "S" and not bust:
        player_move = input("[H]it or [S]tand?").upper()
        if player_move == "H":
            players_hand.append(deck.pop())
            bust = is_bust(players_hand)
        print(LINE)
        print("Dealers Hand: [Face Down] [" + cardgames.get_card_name(dealers_hand[1]) + "]")
        print(cardgames.get_hand_text("Players", players_hand))
        if bust:
            print("You're bust sucka!")
            print(cardgames.get_hand_text("Dealers", dealers_hand))
            print(cardgames.get_hand_text("Players", players_hand))
            return

    # Dealer play phase:
    print("Dealer Hand: [Face Down] and [" + cardgames.get_card_name(dealers_hand[1]) + "]")
    print(cardgames.get_hand_text("Players", players_hand))
    time.sleep(0.5)
    print(LINE)
    time.sleep(0.5)
    print(cardgames.get_hand_text("Dealers", dealers_hand))
    print(cardgames.get_hand_text("Players", players_hand))
    while not is_dealer_stand_hand(dealers_hand):
        dealers_hand.append(deck.pop())
        time.sleep(0.5)
        print(LINE)
        time.sleep(0.5)
        print(cardgames.get_hand_text("Dealers", dealers_hand))
        print(cardgames.get_hand_text("Players", players_hand))
        if is_bust(dealers_hand):
            print("Dealer is bust. You win!")
            return

    # Player and Dealer both stand (neither bust), compare hands:
    player_hand_value = hand_sum(players_hand, True)
    if player_hand_value > 21:
        player_hand_value = hand_sum(players_hand, False)

    dealers_hand_value = hand_sum(dealers_hand, True)
    if dealers_hand_value > 21:
        dealers_hand_value = hand_sum(dealers_hand, False)

    if dealers_hand_value == player_hand_value:
        print("It's a push!")
    elif player_hand_value > dealers_hand_value:
        print("You win!")
    else:
        print("You lose!")


# Start playing & play again loop:
playing = True
while playing:
    print(LINE)
    play_blackjack()
    playing = input("Want to play again? (Y/N)").upper() == "Y"
