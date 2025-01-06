package tests

import (
	"testing"

	"github.com/RomanGoEmpire/the-game/src/model"
)

const (
	UpPile   = 0
	DownPile = 3
)

func freshGame() model.Game {
	var game model.Game
	return game.New()
}

func TestDraw(t *testing.T) {
	game := freshGame()

	amount := 2
	newLength := len(game.DrawPile) - amount

	want := amount
	got := len(game.Draw(amount))
	gotLeft := len(game.DrawPile)
	if got != want || (newLength != gotLeft) {
		t.Errorf("\nWant Amount:\t%v\nGot Amount:\t%s%v%s\nWant Left:\t%d\nGot Left:\t%s%d%s", want, RED, got, RESET, newLength, RED, gotLeft, RESET)
	}
}

func TestTopCard(t *testing.T) {
	game := freshGame()

	want := model.Card(1)
	got := game.TopCard(0)

	if want != got {
		FormatErrorMessage(t, want, got)
	}
}

func TestTopCards(t *testing.T) {
	game := freshGame()

	want := [4]model.Card{1, 1, 100, 100}
	got := game.TopCards()

	if want != got {
		FormatErrorMessage(t, want, got)
	}
}

func TestValidMove(t *testing.T) {
	game := freshGame()

	t.Run("Valid Move up", func(t *testing.T) {
		want := true
		got := game.ValidMove(2, UpPile)
		if want != got {
			FormatErrorMessage(t, want, got)
		}
	})

	t.Run("Valid Move because of jump down", func(t *testing.T) {
		game.Piles[UpPile] = append(game.Piles[UpPile], 12)
		want := true
		got := game.ValidMove(2, UpPile)
		if want != got {
			FormatErrorMessage(t, want, got)
		}
	})
	t.Run("Valid Move because of jump up", func(t *testing.T) {
		game.Piles[DownPile] = append(game.Piles[DownPile], 80)

		want := true
		got := game.ValidMove(90, DownPile)
		if want != got {
			FormatErrorMessage(t, want, got)
		}
	})
	t.Run("Invalid Move because there is a higher card and jump is not possible", func(t *testing.T) {
		game.Piles[UpPile] = append(game.Piles[UpPile], 20)

		want := false
		got := game.ValidMove(2, UpPile)
		if want != got {
			FormatErrorMessage(t, want, got)
		}
	})

	t.Run("Invalid Move because there is a smaller card and jump is not possible", func(t *testing.T) {
		game.Piles[DownPile] = append(game.Piles[DownPile], 90)

		want := false
		got := game.ValidMove(95, DownPile)
		if want != got {
			FormatErrorMessage(t, want, got)
		}
	})

}

func TestAddMove(t *testing.T) {
	game := freshGame()

	t.Run("Valid place on up pil", func(t *testing.T) {
		err := game.PlaceCard(10, UpPile)
		if err != nil {
			FormatErrorMessage(t, "No Error", err)
		}
	})
	t.Run("Valid place on down pile", func(t *testing.T) {
		err := game.PlaceCard(90, DownPile)
		if err != nil {
			FormatErrorMessage(t, "No Error", err)
		}
	})

	t.Run("Invalid place on up pile", func(t *testing.T) {
		err := game.PlaceCard(5, UpPile)
		if err == nil {
			FormatErrorMessage(t, "Error", "No Error")
		}
	})

	t.Run("Invalid plac on down pile", func(t *testing.T) {
		err := game.PlaceCard(95, DownPile)
		if err == nil {
			FormatErrorMessage(t, "Error", "No Error")
		}
	})
}
