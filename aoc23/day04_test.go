package aoc23

import (
	"io"
	"slices"
	"strings"
	"testing"
)

type Card struct {
	winning []int
	numbers []int
	matches int
}

func parseCard(s string) Card {
	parts := strings.FieldsFunc(s, func(r rune) bool { return r == ':' || r == '|' })
	winning := transform(strings.Fields(parts[1]), requireInt)
	slices.Sort(winning)
	numbers := transform(strings.Fields(parts[2]), requireInt)
	return Card{winning, numbers, -1}
}

func (c *Card) winners() int {
	if c.matches < 0 {
		c.matches = quantify(c.numbers, func(n int) bool {
			_, found := slices.BinarySearch(c.winning, n)
			return found
		})
	}
	return c.matches

}

func cardPoints(r io.Reader) int {
	score := 0
	cards := parseLines(r, parseCard)
	for _, card := range cards {
		winners := card.winners()
		if winners > 0 {
			score += pow(2, winners-1)
		}
	}
	return score
}

func countCards(cards []Card) int {
	sum := 0
	for i := range cards {
		winners := cards[i].winners()
		next := i + 1
		sum += 1 + countCards(cards[next:next+winners])
	}
	return sum
}

func cardCount(r io.Reader) int {
	cards := parseLines(r, parseCard)
	return countCards(cards)
}

func TestDay04(t *testing.T) {
	example := `
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
`
	assert(t, 13, run(cardPoints, inputString(example)))
	assert(t, 32001, run(cardPoints, inputFile(4)))

	assert(t, 30, run(cardCount, inputString(example)))
	assert(t, 5037841, run(cardCount, inputFile(4)))
}
