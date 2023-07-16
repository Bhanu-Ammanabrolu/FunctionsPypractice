"""Our Blackjack House Rules

The deck is unlimited in size.
There are no jokers.
The Jack/Queen/King all count as 10.
The Ace can count as 11 or 1.
Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
The cards in the list have equal probability of being drawn.
Cards are not removed from the deck as they are drawn."""

import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def random_cards_deck(no_of_cards):
    for _ in range(no_of_cards):
        return random.choice(cards)


def compare(user_score, computer_score):
    # Bug fix. If you and the computer are both over, you lose.
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"

    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


game_on = True

while game_on:
    start_game = input("Do you want have a game of Blackjack.? Type 'y' or 'n' ")
    if start_game == "y":
        user_cards = []
        computer_cards = []

        for _ in range(2):
            user_cards.append(random_cards_deck(2))
            computer_cards.append(random_cards_deck(2))

        print(f"{user_cards}  user_score = {sum(user_cards)}  \n computer first card is {computer_cards[0]}")
        user_game_on = input("Type 'y' for another card or 'n' to pass:")
        if user_game_on == "y":
            user_cards.append(random_cards_deck(1))
            print(f"{user_cards}  user_score = {sum(user_cards)}  \n computer first card is {computer_cards[0]}")
        else:
            print(f"{user_cards}  user_score = {sum(user_cards)}  \n computer final score is {sum(computer_cards)}")
            result = compare(sum(user_cards), sum(computer_cards))
            print(result)
    else:
        break
