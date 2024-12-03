package aoc24

import (
	"io"
	"strings"
	"testing"
)

func parseMul(r io.Reader, enabledOnly bool) int {
	b, _ := io.ReadAll(r)
	text := string(b)
	const (
		do   = "do()"
		dont = "don't()"
		mul  = "mul("
	)
	match := func(i int, fragment string) bool {
		start := i - len(fragment) + 1
		return start > -1 && text[start:i+1] == fragment
	}
	var (
		sum         = 0
		enabled     = true
		multiplying = false
		buf         strings.Builder
	)
	for i, c := range text {
		if match(i, do) {
			enabled = true
		} else if match(i, dont) {
			enabled = false
		} else if (enabled || !enabledOnly) && match(i, mul) {
			buf.Reset()
			multiplying = true
		} else if multiplying {
			if c == ')' {
				parts := strings.SplitN(buf.String(), ",", 2)
				sum += atoi(parts[0]) * atoi(parts[1])
				multiplying = false
			} else if isDigit(c) || c == ',' {
				buf.WriteRune(c)
			} else {
				multiplying = false
			}
		}
	}
	return sum
}

func TestDay03(t *testing.T) {
	example1 := `xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))`
	check(t, 161, partial(parseMul, false), inputString(example1))
	check(t, 183669043, partial(parseMul, false), inputFile(3))
	example2 := `xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))`
	check(t, 48, partial(parseMul, true), inputString(example2))
	check(t, 59097164, partial(parseMul, true), inputFile(3))
}
