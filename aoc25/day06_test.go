package aoc25

import (
	"bufio"
	"bytes"
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

func homework2(r io.Reader) int {
	var lines [][]rune
	scanner := bufio.NewScanner(r)
	for scanner.Scan() {
		lines = append(lines, runes(scanner.Text()))
	}
	var (
		ops  []rune
		cols []int
	)
	for i, op := range lines[len(lines)-1] {
		if op == ' ' {
			continue
		}
		cols = append(cols, i)
		ops = append(ops, op)
	}
	var (
		buf   bytes.Buffer
		total int
	)
	for i, start := range cols {
		end := len(lines[0])
		if i < len(cols)-1 {
			end = cols[i+1] - 1
		}
		sum := 0
		for j := start; j < end; j++ {
			buf.Reset()
			for _, line := range lines[:len(lines)-1] {
				d := line[j]
				if d == ' ' {
					continue
				}
				buf.WriteRune(d)
			}
			n := atoi(buf.String())
			switch ops[i] {
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
	check(t, 3263827, homework2, readString(example))
	check(t, 8486156119946, homework2, readInput(6))
}
