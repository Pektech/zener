"""All things related to the cards"""
from random import shuffle

cards = [ "cross", "circle", "square", "waves", "star",] * 5


def shuffled_cards(cards):
    shuffle(cards)
    return cards



