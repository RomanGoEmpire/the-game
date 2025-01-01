from icecream import ic

from src.game import Game

if __name__ == "__main__":
    game = Game()
    ic(game.draw_pile)
    ic(game.draw_card())
    ic(len(game.draw_pile))
