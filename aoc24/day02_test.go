package aoc24

import (
	"io"
	"testing"
)

func canChange(from, to int, increasing bool) bool {
	if abs(from-to) < 1 || abs(from-to) > 3 {
		return false
	}
	if increasing {
		return from < to
	}
	return from > to
}

func isSafe(report []int) bool {
	increasing := false
	for i := 0; i < len(report)-1; i++ {
		a := report[i]
		b := report[i+1]
		if i == 0 && a < b {
			increasing = true
		}
		if !canChange(a, b, increasing) {
			return false
		}
	}
	return true
}

func countSafeReports(r io.Reader, canSkip bool) int {
	reports := parseLines(r, numbers)
	count := 0
	for _, report := range reports {
		if isSafe(report) {
			count++
		} else if canSkip {
			for i := range report {
				if isSafe(remove(report, i)) {
					count++
					break
				}
			}
		}
	}
	return count
}

func TestDay02(t *testing.T) {
	example := `
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
`
	check(t, 2, partial(countSafeReports, false), inputString(example))
	check(t, 564, partial(countSafeReports, false), inputFile(2))
	check(t, 4, partial(countSafeReports, true), inputString(example))
	check(t, 604, partial(countSafeReports, true), inputFile(2))
}
