package aoc25

import (
	"io"
	"strings"
	"testing"
)

func homework(r io.Reader) int {
	var (
		grid [][]int
		ops  []rune
	)
	lines(r, func(line string) {
		if strings.ContainsFunc(line, isDigit) {
			grid = append(grid, numbers(line))
		} else {
			for op := range strings.FieldsSeq(line) {
				ops = append(ops, rune(op[0]))
			}
		}
	})
	total := 0
	for x := range grid[0] {
		sum := 0
		for y := range grid {
			n := grid[y][x]
			switch ops[x] {
			case '+':
				sum += n
			case '*':
				if sum == 0 {
					sum = 1
				}
				sum *= n
			}
		}
		total += sum
	}
	return total
}

func TestDay06(t *testing.T) {
	example := `
123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +
`
	check(t, 4277556, homework, readString(example))
	check(t, 4951502530386, homework, readInput(6))
}
