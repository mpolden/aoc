package aoc25

import (
	"io"
	"testing"
)

func countSplits(r io.Reader) int {
	var (
		grid  = parseLines(r, runes)
		stack []Point
	)
	for x := range grid[0] {
		if grid[0][x] == 'S' {
			stack = append(stack, Point{x, 0})
			break
		}
	}
	var (
		visited Set[Point]
		h, w    = len(grid), len(grid[0])
		total   = 0
	)
	for len(stack) > 0 {
		p := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		for ; p.Within(w, h); p = p.Step(directionDown, 1) {
			if grid[p.y][p.x] != '^' {
				visited.Add(p)
				continue
			}
			adjacent := []Point{
				p.Step(directionLeft, 1),
				p.Step(directionRight, 1),
			}
			split := false
			for _, ap := range adjacent {
				if visited.Contains(ap) {
					continue
				}
				split = true
				stack = append(stack, ap)
			}
			if split {
				total++
			}
			break
		}
	}
	return total
}

func TestDay07(t *testing.T) {
	example := `
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
`
	check(t, 21, countSplits, readString(example))
	check(t, 1642, countSplits, readInput(7))
}
