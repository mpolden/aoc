package aoc24

import (
	"io"
	"testing"
)

func rotate(d Direction) Direction {
	switch d {
	case directionUp:
		return directionRight
	case directionRight:
		return directionDown
	case directionDown:
		return directionLeft
	case directionLeft:
		return directionUp
	}
	panic("invalid direction")
}

func findPath(start Point, grid [][]rune) *Set[Point] {
	width, height := len(grid[0]), len(grid)
	visited := &Set[Point]{}
	visited.Add(start)
	direction := directionUp
	for {
		next := start.Step(direction, 1)
		if !next.Within(width, height) {
			break
		}
		if grid[next.y][next.x] == '#' {
			direction = rotate(direction)
		} else {
			start = next
			visited.Add(start)
		}
	}
	return visited
}

func findGuard(grid [][]rune) Point {
	var guard Point
	for y, row := range grid {
		for x, c := range row {
			if c == '^' {
				guard = Point{x, y}
				break
			}
		}
	}
	return guard
}

func countPositions(r io.Reader) int {
	grid := parseLines(r, runes)
	guard := findGuard(grid)
	return findPath(guard, grid).Len()
}

func countObstaclePositions(r io.Reader) int {
	grid := parseLines(r, runes)
	origin := findGuard(grid)
	path := findPath(origin, grid)
	width, height := len(grid[0]), len(grid)
	// Try placing an obstacle at each visited position, excluding original position
	count := 0
	var visited Set[Pose]
	for obstacle := range path.All() {
		if obstacle.Equal(origin) {
			continue
		}
		visited.Clear()
		direction := directionUp
		guard := origin
		for {
			next := guard.Step(direction, 1)
			if !next.Within(width, height) {
				break
			}
			if grid[next.y][next.x] == '#' || next.Equal(obstacle) {
				pose := Pose{guard, direction}
				if visited.Contains(pose) {
					count++ // Reached same point and direction twice
					break
				} else {
					visited.Add(pose)
				}
				direction = rotate(direction)
			} else {
				guard = next
			}
		}
	}
	return count
}

func TestDay06(t *testing.T) {
	example := `
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
`
	check(t, 41, countPositions, readString(example))
	check(t, 5177, countPositions, readFile(6))
	check(t, 6, countObstaclePositions, readString(example))
	check(t, 1686, countObstaclePositions, readFile(6))
}
