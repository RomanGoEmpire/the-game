import pytest

from src.game import Game


def test_is_valid_placement():
    game = Game()

    # Move is valid
    assert game.is_valid_placement(2, 0)
    assert game.is_valid_placement(98, 2)

    # Move is invalid
    game._piles[0].append(10)
    game._piles[2].append(90)

    assert game.is_valid_placement(2, 0) is False
    assert game.is_valid_placement(98, 2) is False

    # Placement is a jump

    game._piles[0].append(15)
    game._piles[2].append(85)

    assert game.is_valid_placement(5, 0)  # jump up
    assert game.is_valid_placement(95, 0)  # jump down

    # Card is invalid
    with pytest.raises(AssertionError, match="Card must be between 2 and 99"):
        game.is_valid_placement(0, 0)

    with pytest.raises(AssertionError):
        game.is_valid_placement(10, 0)


def test_place_card():
    game = Game()

    # Card is on draw pile and therefore not allowed
    with pytest.raises(AssertionError):
        game.place_card(2, 0)

    # Valid Placement
    game.draw_pile.remove(2)
    game.place_card(2, 0)
    assert game.top_of_pile(0) == 2

    # Valid jump up

    game.draw_pile.remove(10)
    game.draw_pile.remove(20)

    game.place_card(20, 0)
    game.place_card(10, 0)

    assert game.top_of_pile(0) == 10

    # Valid jump down

    game.draw_pile.remove(90)
    game.draw_pile.remove(80)

    game.place_card(90, 2)
    game.place_card(80, 2)

    assert game.top_of_pile(2) == 80
