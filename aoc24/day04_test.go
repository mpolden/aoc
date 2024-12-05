package aoc24

import (
	"io"
	"testing"
)

type Point struct{ x, y int }

type Direction int

const (
	topLeft Direction = iota
	top
	topRight
	left
	right
	bottomLeft
	bottom
	bottomRight
)

func path(start Point, distance int, direction Direction, height, width int) []Point {
	x, y := start.x, start.y
	path := []Point{}
	for d := 1; d <= distance; d++ {
		var p Point
		switch direction {
		case topLeft:
			p.x, p.y = x-d, y-d
		case top:
			p.x, p.y = x, y-d
		case topRight:
			p.x, p.y = x+d, y-d
		case left:
			p.x, p.y = x-d, y
		case right:
			p.x, p.y = x+d, y
		case bottomLeft:
			p.x, p.y = x-d, y+d
		case bottom:
			p.x, p.y = x, y+d
		case bottomRight:
			p.x, p.y = x+d, y+d
		default:
			panic("invalid direction")
		}
		if p.x < 0 || p.y < 0 || p.x >= width || p.y >= height {
			break
		}
		path = append(path, p)
	}
	return path
}

func countWords(r io.Reader, mas bool) int {
	grid := parseLines(r, runes)
	hasWord := func(path []Point, word string) bool {
		if len(path) != len(word) {
			return false
		}
		for i, p := range path {
			if grid[p.y][p.x] != rune(word[i]) {
				return false
			}
		}
		return true
	}
	width, height := len(grid), len(grid[0])
	count := 0
	for y, row := range grid {
		for x, c := range row {
			point := Point{x, y}
			if !mas {
				word := "XMAS"
				for d := range bottomRight + 1 {
					p := []Point{point}
					p = append(p, path(point, len(word)-1, d, width, height)...)
					if hasWord(p, word) {
						count++
					}
				}
			} else if c == 'A' {
				// Forward diagonal
				word1, word2 := "MAS", "SAM"
				p := path(point, 1, topLeft, width, height)
				p = append(p, point)
				p = append(p, path(point, 1, bottomRight, width, height)...)
				if hasWord(p, word1) || hasWord(p, word2) {
					// Backward diagonal
					p = path(point, 1, topRight, width, height)
					p = append(p, point)
					p = append(p, path(point, 1, bottomLeft, width, height)...)
					if hasWord(p, word1) || hasWord(p, word2) {
						count++
					}
				}
			}
		}
	}
	return count
}

func TestDay04(t *testing.T) {
	example1 := `
....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX
`
	check(t, 18, partial(countWords, false), readString(example1))
	check(t, 2534, partial(countWords, false), readFile(4))
	example2 := `
.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........
`
	check(t, 9, partial(countWords, true), readString(example2))
	check(t, 1866, partial(countWords, true), readFile(4))
}
