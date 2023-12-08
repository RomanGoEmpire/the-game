from stack import Stack
from players import Player, RandomPlayer


class Game:
    def __init__(self, players: list[Player]) -> None:
        self.players = players
        self.stack = Stack()
        self.current_player = players[0]

    def __str__(self) -> str:
        return f"""Players: {self.players}
    Stack: {self.stack.stack.get("cards")}
    Remaining Cards: {len(self.stack.draw_pile)}
    """

    def next_player(self) -> Player:
        index = (self.players.index(self.current_player) + 1) % len(self.players)
        self.current_player = self.players[index]
        return self.players[index]

    def draws_card(self, player: Player) -> None:
        amount = 6 - len(player.hand)
        new_cards = self.stack.draw_card(amount)
        player.draw_card(new_cards)

    def deal_cards(self) -> None:
        for player in self.players:
            self.draws_card(player)

    def play_round(self) -> None:
        print(f"Its {self.current_player}'s turn.")
        while True:
            if len(self.current_player.hand) == 0:
                print(f"{self.current_player} has no cards left.")
                break

            # Play card
            card, index = self.current_player.play_card(self.stack)
            try:
                self.stack.place_card(card, index)
                self.current_player.hand.remove(card)
            except ValueError as e:
                print(e)
                raise ValueError

            # Stop turn
            if len(self.current_player.hand) <= 4:
                stop_turn = self.current_player.continue_turn()
                if stop_turn:
                    # Draw card
                    if len(self.stack.draw_pile) == 0:
                        print("No cards left in draw pile.")
                    else:
                        self.draws_card(self.current_player)
                    print(f"{self.current_player} stops turn.")

                    break

                print(f"{self.current_player} continues turn.")
            print(f"You have to play at least 2 cards.")


if __name__ == "__main__":
    players = [RandomPlayer("Random"), RandomPlayer("Random2")]
    game = Game(players)
    game.deal_cards()
    for i in range(10):
        print(f"Round {i}")
        game.play_round()
        game.next_player()
        print(game)
