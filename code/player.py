class Player:
    def __init__(self, name="Player") -> None:
        self.name = name
        self.hand = []

    def __str__(self) -> str:
        return f"{self.name} has {self.hand} in hand."

    def sort_hand(self) -> None:
        self.hand.sort()

    # ! Add logic in Child
    def play_card(self) -> int:
        pass

    # ! Add Logic in Child
    def block_stack(self, stack) -> list(int):
        pass
