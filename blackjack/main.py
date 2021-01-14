import random

import blackjack_art


def deal_cards():
    # Return random card from the deck
    cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    
    # If blackjack condition occur return 0 to indicate the occurrence of the event
    if (sum(cards) == 21 and len(cards) == 2):
        return 0
    
    # if sum of cards is greater than 21 and 11 is contained, then remove 11 and change it to 1
    if (11 in cards and sum(cards) > 21):
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)

def compare(user_score, ai_score):
    if (user_score == ai_score):
        return "It's a Draw 😐"
    elif (ai_score == 0):
        return "You lose! Your opponent has a blackjack 🙁"
    elif (user_score == 0):
        return "You win with a blackjack😇"
    elif (user_score > 21):
        return "You went over, you lose 🤬"
    elif (ai_score > 21):
        return "Your opponent went over, you win 😬"
    elif (user_score > ai_score):
        return "You win 😀"
    else:
        return "You lose 😡"

def play_blackjack():
    print(blackjack_art.logo)
    
    # Initialize cards in hand
    user_cards = []
    ai_cards = []

    # Initialize game state
    game_over = False

    # Deal card to the human and AI player
    for _ in range(2):
        user_cards.append(deal_cards())
        ai_cards.append(deal_cards())

    while (not game_over):
        user_score = calculate_score(user_cards)
        ai_score = calculate_score(ai_cards)
        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    AI's first card: {ai_cards[0]}")
        # Game over if user or ai has a black jack or user has score greater than 21
        if (user_score == 0 or ai_score == 0 or user_score > 21):
            game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if (user_should_deal == "y"):
                user_cards.append(deal_cards())
            else:
                game_over = True

        while (ai_score != 0 and ai_score < 17):
            ai_cards.append(deal_cards())
            ai_score = calculate_score(ai_cards)

        print(f"    Your final cards: {user_cards}, final score: {user_score}")
        print(f"    AI final cards: {ai_cards}, final score: {ai_score}")
        print(compare(user_score, ai_score))

while (input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y"):

    play_blackjack()


