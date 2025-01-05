package tests

import "testing"

const (
	RED   = "\033[36m"
	RESET = "\033[0m"
)

func FormatErrorMessage(t *testing.T, want interface{}, got interface{}) {
	t.Fatalf("\nWant: %v\nGot : %s%v%s", want, RED, got, RESET)
}

func Test(t *testing.T) {
	want := 0
	got := 1
	if want != got {
		FormatErrorMessage(t, want, got)
	}
}
