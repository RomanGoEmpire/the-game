from random import shuffle


class Stack:
    def __init__(self) -> None:
        self.draw_pile = [i for i in range(2, 100)]
        shuffle(self.draw_pile)
        self.stack = {
            "cards": [1, 1, 100, 100],
            "direction": ["up", "up", "down", "down"],
        }

    def __str__(self) -> str:
        return f"Stack: {self.stack}"

    def draw_card(self) -> int:
        return self.draw_pile.pop()
