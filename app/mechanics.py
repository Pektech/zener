""" How the game works using console before splitting up into alexa intents"""
from app.cards import cards, shuffled_cards



CARD_COUNT = 0
DECK = shuffled_cards(cards)
SCORE = 0

"""Test mechanics of game"""
# while CARD_COUNT < 25:
#     choosen_card = DECK[CARD_COUNT]
#     guessed_card = input("choose card")
#
#     if guessed_card == choosen_card:
#         SCORE += 1
#     CARD_COUNT += 1
#
# print(f'You scored {SCORE}')

