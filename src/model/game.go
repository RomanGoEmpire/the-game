package model

import (
	"fmt"
	"math/rand"
)

const (
	JUMP_AMOUNT = 10
	TOTAL_CARDS = 98
)

type Card int

type Game struct {
	DrawPile []Card
	Piles    [4][]Card
}

func NewDrawPile() []Card {
	drawPile := make([]Card, 98)
	for i := 0; i < TOTAL_CARDS; i++ {
		drawPile[i] = Card(i + 2)
	}
	rand.Shuffle(TOTAL_CARDS, func(i int, j int) {
		drawPile[i], drawPile[j] = drawPile[j], drawPile[i]
	})
	return drawPile
}

func (game *Game) New() Game {
	return Game{
		DrawPile: NewDrawPile(),
		Piles: [4][]Card{
			{1},
			{1},
			{100},
			{100},
		},
	}
}

func (game *Game) Draw(amount int) []Card {
	drawCards := game.DrawPile[:amount]
	game.DrawPile = game.DrawPile[amount:]
	return drawCards
}

func (game *Game) TopCard(pileIndex int) Card {
	pile := game.Piles[pileIndex]
	return pile[len(pile)-1]
}

func (game *Game) TopCards() [4]Card {
	topCards := [4]Card{}

	for i, pile := range game.Piles {
		topCards[i] = pile[len(pile)-1]
	}
	return topCards
}

func (game *Game) ValidMove(card Card, pileIndex int) bool {
	currentCard := game.TopCard(pileIndex)
	if pileIndex < 2 {
		return currentCard-JUMP_AMOUNT == card || currentCard < card
	} else {
		return currentCard+JUMP_AMOUNT == card || currentCard > card
	}
}

func (deck *Game) PlaceCard(card Card, pileIndex int) error {
	if !deck.ValidMove(card, pileIndex) {
		return fmt.Errorf("Invalid Move onPile %d:\nCurrent Card: %v\bCard: %v", pileIndex, deck.TopCard(pileIndex), card)
	}
	deck.Piles[pileIndex] = append(deck.Piles[pileIndex], card)
	return nil
}
