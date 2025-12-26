package aoc25

import (
	"io"
	"testing"
)

func joltage(r io.Reader, batteries int) int64 {
	banks := parseLines(r, func(line string) []int {
		return transform(runes(line), digit)
	})
	var (
		sum  int64
		last = batteries - 1
	)
	for _, bank := range banks {
		var (
			next    = 0
			choices = len(bank)
		)
		for bat := range batteries {
			joltage := 0
			for i := next; i <= choices-batteries+bat || (bat == last && i < choices); i++ {
				if bank[i] > joltage {
					joltage = bank[i]
					next = i + 1
				}
			}
			p := batteries - bat - 1
			joltage *= max(1, pow(10, p))
			sum += int64(joltage)
		}
	}
	return sum
}

func TestDay03(t *testing.T) {
	example := `
987654321111111
811111111111119
234234234234278
818181911112111
`
	check(t, 357, partial(joltage, 2), readString(example))
	check(t, 17343, partial(joltage, 2), readFile(3))
	check(t, 3121910778619, partial(joltage, 12), readString(example))
	check(t, 172664333119298, partial(joltage, 12), readFile(3))
}
