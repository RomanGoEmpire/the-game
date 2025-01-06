package tests

import (
	"testing"

	"github.com/RomanGoEmpire/the-game/src/model"
)

func TestAddCards(t *testing.T) {
	player := model.Player{}
	player.AddCards([]model.Card{10, 15})
	want := []model.Card{10, 15}
	got := player.Hand
	if !Equal(got, want) {
		FormatErrorMessage(t, want, got)
	}
}

func TestRemoveCard(t *testing.T) {
	player := model.Player{Hand: []model.Card{10, 13}}

	player.RemoveCard(10)
	want := []model.Card{13}
	got := player.Hand

	if !Equal(got, want) || player.AmountToDraw() != 5 {
		FormatErrorMessage(t, want, got)
	}
}

func TestAmountToDraw(t *testing.T) {
	player := model.Player{Hand: []model.Card{10, 13}}
	want := 4
	got := player.AmountToDraw()
	if want != got {
		FormatErrorMessage(t, want, got)
	}
}
