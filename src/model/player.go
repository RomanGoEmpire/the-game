package model

import (
	"slices"
)

const (
	MAX_CARDS = 6
)

type Player struct {
	Name string
	Hand []Card
}

func (player *Player) AddCards(cards []Card) {
	player.Hand = append(player.Hand, cards...)
	slices.Sort(player.Hand)
}

func (player *Player) RemoveCard(cardValue Card) {
	var newHand []Card
	for _, card := range player.Hand {
		if card != cardValue {
			newHand = append(newHand, card)
		}
	}
	player.Hand = newHand
}

// How many Cards are missing.
func (player *Player) AmountToDraw() int {
	return MAX_CARDS - len(player.Hand)
}
