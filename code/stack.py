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
        return (
            f"Stack: {self.stack.get('cards')}\nRemaining Cards: {len(self.draw_pile)}"
        )

    def __repr__(self) -> str:
        return self.__str__()

    def draw_card(self) -> int:
        return self.draw_pile.pop()

    def place_card(self, card: int, index: int) -> None:
        if self.is_legal(card, index):
            print(f"Stack before: {self.stack.get('cards')}")
            print(f"Placing {card} on card {self.stack.get('cards')[index]}")
            self.stack["cards"][index] = card
            print(f"Stack after: {self.stack.get('cards')}")
            print("")
        else:
            raise ValueError(
                f"Card {card} cannot be placed on stack {self.stack[index]}."
            )

    def is_legal(self, card: int, index: int) -> bool:
        if self.stack["direction"][index] == "up":
            return (
                card > self.stack["cards"][index]
                or card == self.stack["cards"][index] - 10
            )
        else:
            return (
                card < self.stack["cards"][index]
                or card == self.stack["cards"][index] + 10
            )
