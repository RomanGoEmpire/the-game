class Player:
    def __init__(self, name="Player") -> None:
        self.name = name
        self.hand = []

    def __str__(self) -> str:
        return f"{self.name}, Hand: {self.hand}"

    def __repr__(self) -> str:
        return self.__str__()

    def sort_hand(self) -> None:
        self.hand.sort()

    # ! Add logic in Child
    def play_card(self, stack) -> (int, int):
        # Return card and index of stack
        pass

    # ! Add Logic in Child
    def block_stack(self, stack) -> list[int]:
        pass

    def draw_card(self, new_cards) -> None:
        print(f"{self.name} draws {new_cards}")
        self.hand += new_cards
        self.sort_hand()

    # ! Add Logic in Child
    def continue_turn(self) -> bool:
        pass
