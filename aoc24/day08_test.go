package aoc24

import (
	"io"
	"testing"
)

func findAntinodes(r io.Reader, includeAll bool) int {
	grid := parseLines(r, runes)
	antennasByFreq := make(map[rune][]Point)
	for y, row := range grid {
		for x, c := range row {
			if c != '.' {
				antennasByFreq[c] = append(antennasByFreq[c], Point{x, y})
			}
		}
	}
	width, height := len(grid[0]), len(grid)
	var antinodes Set[Point]
	for _, antennas := range antennasByFreq {
		for i, a := range antennas {
			for j, b := range antennas {
				if i == j {
					continue
				}
				diff := a.Sub(b)
				if includeAll {
					for antinode := a; antinode.Within(width, height); antinode = antinode.Add(diff) {
						antinodes.Add(antinode)
					}
					for antinode := b; antinode.Within(width, height); antinode = antinode.Sub(diff) {
						antinodes.Add(antinode)
					}
				} else {
					for _, antinode := range []Point{a.Add(diff), b.Sub(diff)} {
						if antinode.Within(width, height) {
							antinodes.Add(antinode)
						}
					}
				}
			}
		}
	}
	return antinodes.Len()
}

func TestDay08(t *testing.T) {
	example := `
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
`
	check(t, 14, partial(findAntinodes, false), readString(example))
	check(t, 364, partial(findAntinodes, false), readFile(8))
	check(t, 34, partial(findAntinodes, true), readString(example))
	check(t, 1231, partial(findAntinodes, true), readFile(8))
}
