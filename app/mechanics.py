""" How the game works using console before splitting up into alexa intents"""
from app.cards import cards, shuffled_cards



CARD_COUNT = 0
DECK = shuffled_cards(cards)
SCORE = 0
DECK_SIZE = 25

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

def final_score(score):
    if score < 2 :
        return f"Wow either you are really unlucky or have " \
               f"some sort of anti-clairvoyance skill. You scored {score} "
    elif 3 <= score <= 10 :
        return f" Not a bad score but the average person scores between 3 and 8. " \
               f"Your final score was {score}. yeah pretty average"
    else:
        return f"Wow {score} that is a really high score. Maybe you should play the lottery"