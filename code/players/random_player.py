from random import randint
import random

from .player import Player


class RandomPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def play_card(self, stack):
        card = random.choice(self.hand)
        index = randint(0, 3)
        if stack.is_legal(card, index):
            print(f"{self.name} wants to play {card} on stack {index}.")
            return card, index
        else:
            return self.play_card(stack)
