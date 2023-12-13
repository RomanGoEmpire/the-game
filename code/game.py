from .stack import Stack
from .players import Player, RandomPlayer


class Game:
    def __init__(self, players: list[Player]) -> None:
        self.players = players
        self.stack = Stack()
        self.current_player = players[0]
        self.game_over = False
        self.won = False

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
            # No cards left
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
                print(f"You cant play {card} on {self.stack.stack.get('cards')[index]}.")
                raise ValueError

            # has to play at least 2 cards
            if len(self.current_player.hand) > 4:
                # player has to play at least 2 cards but cant play any
                if not self.current_player.can_play(self.stack):
                    self.game_over = True
                    print(f"{self.current_player} has to play at least 2 cards but cant play any.")
                    break
                print(f"{self.current_player} continues turn.")
                continue
            
            
            continue_turn = self.current_player.continue_turn()
            if continue_turn:
                print(f"{self.current_player} continues turn.")
                continue
            # refill hand of player
            if len(self.stack.draw_pile) == 0:
                print("No cards left in draw pile.")
            else:
                self.draws_card(self.current_player)
            print(f"{self.current_player} stops turn.")
            break
            
    
    def check_win(self) -> bool:
        # if all players have 0 cards left
        return all([len(player.hand) == 0 for player in self.players])

    def play_game(self) -> None:
        self.deal_cards()
        while not self.game_over:
            self.play_round()
            self.next_player()
            if self.check_win():
                self.game_over = True
                self.won = True
                break
        string_won = "won" if self.won else "lost"
        print(f"Player {string_won} the game!")
        
        
        
            
