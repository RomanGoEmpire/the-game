package tests

import (
	"fmt"
	"testing"

	"github.com/RomanGoEmpire/the-game/src/model"
)

const (
	RED   = "\033[36m"
	RESET = "\033[0m"
)

func FormatErrorMessage(t testing.TB, want, got interface{}) {
	t.Helper()
	t.Errorf("\nWant:\t%v\nGot:\t%s%v%s", want, RED, got, RESET)
}

func Equal(got []model.Card, want []model.Card) bool {
	if len(got) != len(want) {
		return false
	}
	for index, _ := range got {
		if got[index] != want[index] {
			fmt.Println(got[index], want[index])
			return false
		}
	}
	return true
}
