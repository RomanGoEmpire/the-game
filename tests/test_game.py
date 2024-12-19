import pytest

from src.game import Game


def test_is_valid_placement():
    game = Game()

    # ? Move is valid
    assert game.is_valid_placement(2, 0)
    assert game.is_valid_placement(98, 2)

    # ? Move is invalid
    game.piles[0].append(10)
    game.piles[2].append(90)

    assert game.is_valid_placement(2, 0)
    assert game.is_valid_placement(98, 2) is False

    # ? Placement is a jump

    game.piles[0].append(15)
    game.piles[2].append(85)

    assert game.is_valid_placement(5, 0)
    assert game.is_valid_placement(95, 0)

    # ? Card is invalid
    with pytest.raises(AssertionError, match="Card must be between 2 and 99"):
        game.is_valid_placement(0, 0)

    with pytest.raises(AssertionError):
        game.is_valid_placement(10, 0)


def test_place_card():
    game = Game()

    # ? Card is on draw pile and therefore not allowed
    with pytest.raises(AssertionError):
        game.place_card(2, 0)

    game.draw_pile.remove(2)
    game.place_card(2, 0)
    assert game.top_of_pile(0) == 2
