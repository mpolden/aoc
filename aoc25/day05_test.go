package aoc25

import (
	"cmp"
	"io"
	"slices"
	"strings"
	"testing"
)

func parseIngredients(r io.Reader) ([]Range, []int) {
	var (
		specs      []Range
		candidates []int
	)
	lines(r, func(line string) {
		if strings.Contains(line, "-") {
			specs = append(specs, rangeOf(line))
		} else if line != "" {
			candidates = append(candidates, atoi(line))
		}
	})
	return specs, candidates
}

func countFresh(r io.Reader) int {
	specs, candidates := parseIngredients(r)
	count := 0
	for _, c := range candidates {
		for _, spec := range specs {
			if spec.Contains(c) {
				count++
				break
			}
		}
	}
	return count
}

func inclusiveLen(start, end int) int { return max(0, 1+(end-start)) }

func allFresh(r io.Reader) int {
	specs, _ := parseIngredients(r)
	slices.SortFunc(specs, func(a, b Range) int {
		return cmp.Or(cmp.Compare(a.start, b.start), cmp.Compare(a.end, b.end))
	})
	var (
		last  = specs[len(specs)-1]
		total = inclusiveLen(last.start, last.end)
	)
	for i := 0; i < len(specs)-1; i++ {
		var (
			j    = i + 1
			cur  = specs[i]
			next = specs[j]
		)
		if cur.end > next.end {
			specs[j].end = cur.end
		}
		if cur.start == next.start {
			continue
		}
		var (
			size     = inclusiveLen(cur.start, cur.end)
			overflow = inclusiveLen(next.start, cur.end)
		)
		total += size - overflow
	}
	return total
}

func TestDay05(t *testing.T) {
	example := `
3-5
10-14
16-20
12-18

1
5
8
11
17
32
`
	check(t, 3, countFresh, readString(example))
	check(t, 733, countFresh, readInput(5))
	check(t, 14, allFresh, readString(example))
	check(t, 345821388687084, allFresh, readInput(5))
}
