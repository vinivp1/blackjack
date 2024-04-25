import random
from art import logo

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
        print("It's a draw!!!")
    elif your_score == 0:
        print("You win 🥇😜")
    elif computer_score == 0:
        print("You lose 🥈")
    elif your_score > 21:
        print("You lose 🥈")
    elif computer_score > 21:
        print("You win 🥇😜")
    else:
        if your_score > computer_score:
            print("You win 🥇😜")
        else:
            print("You lose 🥈")

def game():
    your_cards = []
    computer_cards = []
    is_game_over = False
    to_continue = True
    print(logo)

    for _ in range(2):
        your_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    your_score = calculate_score(your_cards)
    computer_score = calculate_score(computer_cards)

    print(f"Your cards: {your_cards}, current score: {your_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    if your_score == 0 or computer_score == 0 or your_score > 21 or computer_score > 21:
        is_game_over = True
        to_continue = False
    if to_continue == False:
        compare()

    while to_continue:
        if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
            your_cards.append(deal_cards())
            your_score = calculate_score(your_cards)
            print(f"Your cards: {your_cards}, current score: {your_score}")
            print(f"Computer's first card: {computer_cards[0]}")
        else:
            to_continue = False

            while computer_score < 17:
                computer_cards.append(deal_cards())
            computer_score = calculate_score(computer_cards)

            return computer_score , your_score

            compare()

            blackjack()

def blackjack():
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
        game()

blackjack()