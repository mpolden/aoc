package aoc24

import (
	"io"
	"slices"
	"strings"
	"testing"
)

func totalDistance(r io.Reader) int {
	var left []int
	var right []int
	lines(r, func(s string) {
		fields := strings.Fields(s)
		left = append(left, atoi(fields[0]))
		right = append(right, atoi(fields[1]))
	})
	slices.Sort(left)
	slices.Sort(right)
	distance := 0
	for i := range len(left) {
		distance += abs(left[i] - right[i])
	}
	return distance
}

func similarityScore(r io.Reader) int {
	var left []int
	var right []int
	lines(r, func(s string) {
		fields := strings.Fields(s)
		left = append(left, atoi(fields[0]))
		right = append(right, atoi(fields[1]))
	})
	score := 0
	for _, l := range left {
		occurences := 0
		for _, r := range right {
			if l == r {
				occurences++
			}
		}
		score += l * occurences
	}
	return score
}

func TestDay01(t *testing.T) {
	example := `
3   4
4   3
2   5
1   3
3   9
3   3
`
	check(t, 11, totalDistance, inputString(example))
	check(t, 1765812, totalDistance, inputFile(1))
	check(t, 31, similarityScore, inputString(example))
	check(t, 20520794, similarityScore, inputFile(1))
}
