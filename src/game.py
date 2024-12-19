import random

JUMP_DISTANCE = 10


class Game:
    def __init__(self):
        self.draw_pile = [i for i in range(1, 99)]
        random.shuffle(self.draw_pile)

        self.piles = [[1], [1], [100], [100]]  # up, up, down, down

    def top_of_pile(self, pile: int) -> int:
        assert 0 <= pile < len(self.piles)
        return self.piles[pile][-1]

    def cards_left(self) -> int:
        return len(self.draw_pile)

    def is_valid_placement(self, card: int, pile: int) -> bool:
        assert 2 <= card <= 99, "Card must be between 2 and 99"
        assert any(card in p for p in self.piles) is False, "Card is already in a pile"
        last_card = self.piles[pile][-1]

        if pile in [0, 1]:  # * pile goes up
            return card > last_card or last_card - JUMP_DISTANCE == card
        else:  # * pile goes down
            return card < last_card or last_card + JUMP_DISTANCE == card

    def draw_card(self) -> int:
        assert self.draw_pile, "No more cards left"
        return self.draw_pile.pop()

    def place_card(self, card: int, pile: int) -> None:
        assert self.is_valid_placement(card, pile)
        assert card not in self.draw_pile, "Card is in draw pile"

        self.piles[pile].append(card)
