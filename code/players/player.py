class Player:
    def __init__(self, name="Player") -> None:
        self.name = name
        self.hand = []

    def __str__(self) -> str:
        return f"{self.name}, {len(self.hand)} cards left"

    def __repr__(self) -> str:
        return self.__str__()

    def sort_hand(self) -> None:
        self.hand.sort()
        
    # ! Add logic in Child
    def play_card(self, stack) -> (int, int):
        # Return card and index of stack
        raise NotImplementedError

    # ! Add Logic in Child
    def block_stack(self, stack) -> list[int]:
        # Return cards to block stack
        raise NotImplementedError

    def draw_card(self, new_cards) -> None:
        print(f"{self.name} draws {len(new_cards)}")
        self.hand += new_cards
        self.sort_hand()

    # ! Add Logic in Child
    def continue_turn(self) -> bool:
        # Return True if player wants to continue turn
        raise NotImplementedError
    
    def can_play(self, stack) -> bool:
        for card in self.hand:
            for index in range(4):
                if stack.is_legal(card, index):
                    return True
        return False
