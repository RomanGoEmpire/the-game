package main

import (
	"fmt"

	"github.com/RomanGoEmpire/the-game/src/model"
)

func main() {
	var game model.Game
	game = game.New()

	playerOne := model.Player{Name: "Player One"}

	drawCards := game.Draw(playerOne.AmountToDraw())
	playerOne.AddCards(drawCards)
	fmt.Println(playerOne)

	fmt.Println(game.Piles)
}
