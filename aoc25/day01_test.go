package aoc25

import (
	"io"
	"testing"
)

func findPassword(r io.Reader, perClick bool) int {
	offsets := parseLines(r, func(s string) int {
		n := atoi(s[1:])
		if s[0] == 'L' {
			n = -n
		}
		return n
	})
	var (
		pos    = 50
		atZero = 0
	)
	for _, offset := range offsets {
		n := 1
		if offset < 0 {
			n = -1
		}
		turns := abs(offset)
		for turn := range turns {
			pos += n
			switch pos {
			case 100:
				pos = 0
			case -1:
				pos = 99
			}
			if pos == 0 && (perClick || turn == turns-1) {
				atZero++
			}
		}
	}
	return atZero
}

func TestDay01(t *testing.T) {
	example := `
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
`
	check(t, 3, partial(findPassword, false), readString(example))
	check(t, 1021, partial(findPassword, false), readFile(1))
	check(t, 6, partial(findPassword, true), readString(example))
	check(t, 5933, partial(findPassword, true), readFile(1))
}
