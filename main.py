from code import Game, HumanPlayer

def main():
    # Create players
    players = []
    for i in range(2):
        name = input(f"Player {i+1} name: ")
        players.append(HumanPlayer(name))

    # Create game
    game = Game(players)

    # Deal cards
    game.deal_cards()

    # Play game
    while True:
        print(game)
        game.play_round()
        if len(game.current_player.hand) == 0:
            print(f"{game.current_player} wins!")
            break
        game.next_player()
        
if __name__ == "__main__":
    main()