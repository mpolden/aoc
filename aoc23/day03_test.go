package aoc23

import (
	"io"
	"testing"
)

type Point struct{ x, y int }

func neighbours(point Point, height, width int) *Set[Point] {
	neighbours := Set[Point]{}
	x, y := point.x, point.y
	if x > 0 {
		neighbours.Add(Point{x - 1, y}) // left
	}
	if x < width-1 {
		neighbours.Add(Point{x + 1, y}) // right
	}
	if y > 0 {
		neighbours.Add(Point{x, y - 1}) // top
		if x > 0 {
			neighbours.Add(Point{x - 1, y - 1}) // top-left
		}
		if x < width-1 {
			neighbours.Add(Point{x + 1, y - 1}) // top-right
		}
	}
	if y < height-1 {
		neighbours.Add(Point{x, y + 1}) // bottom
		if x > 0 {
			neighbours.Add(Point{x - 1, y + 1}) // bottom-left
		}
		if x < width-1 {
			neighbours.Add(Point{x + 1, y + 1}) // bottom-right
		}
	}
	return &neighbours
}

func nearSymbol(point Point, grid [][]rune) bool {
	for _, np := range neighbours(point, len(grid), len(grid[0])).Slice() {
		r := grid[np.y][np.x]
		if r != '.' && !isDigit(r) {
			return true
		}
	}
	return false
}

func findGear(point Point, grid [][]rune) *Point {
	for _, np := range neighbours(point, len(grid), len(grid[0])).Slice() {
		if grid[np.y][np.x] == '*' {
			v := np
			return &v
		}
	}
	return nil
}

func findNumber(r io.Reader, consumer func(int, []Point, [][]rune)) {
	grid := parseLines(r, runes)
	for y, row := range grid {
		points := &Set[Point]{}
		number := ""
		parsingNumber := false
		for x, c := range row {
			if isDigit(c) {
				number += string(c)
				points.Add(Point{x, y})
				parsingNumber = x < len(row)-1
			} else {
				parsingNumber = false
			}
			if !parsingNumber && number != "" {
				consumer(atoi(number), points.Slice(), grid)
				points.Reset()
				number = ""
			}
		}
	}
}

func sumPartNumbers(r io.Reader) int {
	sum := 0
	findNumber(r, func(n int, points []Point, grid [][]rune) {
		if some(points, partial(nearSymbol, grid)) {
			sum += n
		}
	})
	return sum
}

func sumGearRatios(r io.Reader) int {
	gears := make(map[Point]*Set[int])
	findNumber(r, func(n int, points []Point, grid [][]rune) {
		for _, p := range points {
			gearPoint := findGear(p, grid)
			if gearPoint == nil {
				continue
			}
			k := *gearPoint
			v, ok := gears[k]
			if !ok {
				v = &Set[int]{}
				gears[k] = v
			}
			v.Add(n)
		}
	})
	sum := 0
	for _, v := range gears {
		if v.Len() > 1 {
			sum += product(v.Slice())
		}
	}
	return sum
}

func TestDay03(t *testing.T) {
	example := `
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
`
	assert(t, 4361, run(sumPartNumbers, inputString(example)))
	assert(t, 528819, run(sumPartNumbers, inputFile(3)))

	assert(t, 467835, run(sumGearRatios, inputString(example)))
	assert(t, 80403602, run(sumGearRatios, inputFile(3)))
}
