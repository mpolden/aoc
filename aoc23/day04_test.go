package aoc23

import (
	"io"
	"regexp"
	"strings"
	"testing"
)

type Card struct {
	id      int
	winners Set[int]
	got     []int
}

func parseCard(s string) Card {
	re := regexp.MustCompile(": | \\| ")
	parts := re.Split(s, -1)
	id := requireInt(strings.Fields(parts[0])[1])
	got := map2(strings.Fields(parts[2]), requireInt)
	winners := Set[int]{}
	winners.AddAll(map2(strings.Fields(parts[1]), requireInt))
	return Card{id, winners, got}
}

func countWinners(card Card) int {
	return frequency(card.got, func(g int) bool { return card.winners.Contains(g) })
}

func cardPoints(r io.Reader) int {
	score := 0
	cards := parseLines(r, parseCard)
	for _, card := range cards {
		winners := countWinners(card)
		if winners > 0 {
			score += pow(2, winners-1)
		}
	}
	return score
}

func countCards(cards []Card) int {
	sum := 0
	for i, card := range cards {
		winners := countWinners(card)
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
