package aoc24

import (
	"io"
	"strings"
	"testing"
)

type Calibration struct {
	Wanted  int64
	Numbers []int64
}

func eval(numbers []int64, operators []rune) int64 {
	acc := numbers[0]
	for i := 0; i < len(numbers)-1; i++ {
		next := numbers[i+1]
		switch operators[i] {
		case '+':
			acc += next
		case '*':
			acc *= next
		case '|':
			digits := 0
			for n := next; n > 0; n /= 10 {
				digits++
			}
			for range digits {
				acc *= 10
			}
			acc += next
		}
	}
	return acc
}

func equationEquals(calibration Calibration, concat bool) bool {
	nops := 2 // 'add' and 'mul'
	if concat {
		nops++ // 'concat'
	}
	slots := len(calibration.Numbers) - 1
	operators := make([]rune, slots)
	combinations := 1
	for range slots {
		combinations *= nops
	}
	for c := 0; c < combinations; c++ {
		ci := c
		for i := 0; i < slots; i++ {
			switch ci % nops {
			case 0:
				operators[i] = '+'
			case 1:
				operators[i] = '*'
			case 2:
				operators[i] = '|'
			}
			ci /= nops
		}
		if eval(calibration.Numbers, operators) == calibration.Wanted {
			return true
		}
	}
	return false
}

func checkCalibrations(r io.Reader, concat bool) int64 {
	calibrations := parseLines(r, func(line string) Calibration {
		parts := strings.SplitN(line, ": ", 2)
		numbers := transform(strings.Fields(parts[1]), atoi64)
		return Calibration{atoi64(parts[0]), numbers}
	})
	var sum int64
	for _, c := range calibrations {
		if equationEquals(c, concat) {
			sum += c.Wanted
		}
	}
	return sum
}

func TestDay07(t *testing.T) {
	example := `
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
`
	check(t, 3749, partial(checkCalibrations, false), readString(example))
	check(t, 303766880536, partial(checkCalibrations, false), readFile(7))
	check(t, 11387, partial(checkCalibrations, true), readString(example))
	check(t, 337041851384440, partial(checkCalibrations, true), readFile(7))
}
