package aoc23

import (
	"io"
	"testing"
)

func findDigits(text string, parseWords bool) []int {
	words := []string{"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"}
	var ints []int
	buf := ""
	for _, c := range text {
		if isDigit(c) {
			n := requireInt(string(c))
			ints = append(ints, n)
		} else if parseWords {
			buf += string(c)
			for i, w := range words {
				if len(buf) >= len(w) && buf[len(buf)-len(w):] == w {
					ints = append(ints, i+1)
					break
				}
			}
		}
	}
	return ints
}

func sumCalibrations(r io.Reader, parseWords bool) int {
	values := parseLines(r, func(s string) []int { return findDigits(s, parseWords) })
	return sum(map2(values, func(ints []int) int { return (ints[0] * 10) + ints[len(ints)-1] }))
}

func TestDay01(t *testing.T) {
	example := `
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
`
	assert(t, 142, run(partial(sumCalibrations, false), inputString(example)))
	assert(t, 55488, run(partial(sumCalibrations, false), inputFile(1)))

	example2 := `
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
`
	assert(t, 281, run(partial(sumCalibrations, true), inputString(example2)))
	assert(t, 55614, run(partial(sumCalibrations, true), inputFile(1)))
}
