package aoc25

import (
	"io"
	"testing"
)

func countRolls(grid [][]rune, remove bool) (int, int) {
	const (
		roll  = '@'
		empty = '.'
	)
	var (
		h, w    = len(grid), len(grid[0])
		count   = 0
		removed = 0
	)
	for y := range grid {
		for x := range grid[y] {
			if grid[y][x] != roll {
				continue
			}
			p := Point{x, y}
			adjacentRolls := 0
			for dir := range directionDownRight + 1 {
				np := p.Step(dir, 1)
				if !np.Within(w, h) {
					continue
				}
				if grid[np.y][np.x] == roll {
					adjacentRolls++
				}
			}
			if adjacentRolls < 4 {
				count++
				if remove {
					grid[p.y][p.x] = empty
					removed++
				}
			}
		}
	}
	return count, removed
}

func processRolls(r io.Reader, remove bool) int {
	grid := parseLines(r, runes)
	sum := 0
	for {
		count, removed := countRolls(grid, remove)
		sum += count
		if removed == 0 {
			break
		}
	}
	return sum
}

func TestDay04(t *testing.T) {
	example := `
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
`
	check(t, 13, partial(processRolls, false), readString(example))
	check(t, 1433, partial(processRolls, false), readInput(4))
	check(t, 43, partial(processRolls, true), readString(example))
	check(t, 8616, partial(processRolls, true), readInput(4))
}
