import random
from art import logo
import os

def deal_cards():
    """Randomize the cards"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Verify the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) < 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(your_score, computer_score):
    if your_score == computer_score:
        return "It's a draw 😕"
    elif your_score == 0:
        return "You win, you have a blackjack 🥇😜"
    elif computer_score == 0:
        return "You lose, the rival have a blackjack 🥈"
    elif your_score > 21:
        return "You lose 🥈"
    elif computer_score > 21:
        return "You win 🥇😜"
    else:
        if your_score > computer_score:
            return "You win 🥇😜"
        else:
            return "You lose 🥈"

def game():
    your_cards = []
    computer_cards = []
    is_game_over = False
    print(logo)

    for _ in range(2):
        your_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    while not is_game_over:
        your_score = calculate_score(your_cards)
        computer_score = calculate_score(computer_cards)

        print(f"   Your cards: {your_cards}, current score: {your_score}")
        print(f"   Computer's first card: {computer_cards[0]}")

        if your_score == 0 or computer_score == 0 or your_score > 21 or computer_score > 21:
            is_game_over = True
        else:
            to_continue = input("Type 'y' to get another card, type 'n' to pass: ")
            if to_continue == "y":
                your_cards.append(deal_cards())
            else:
              is_game_over = True

        while computer_score!= 0  and computer_score<17:
            computer_cards.append(deal_cards())
            computer_score = calculate_score(computer_cards)

    print(f"   Your final hand: {your_cards}, final score: {your_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(your_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    os.system('cls')  # Windows ou os.system('clear') para Linux/macOS
    game()