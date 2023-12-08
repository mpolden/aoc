package aoc23

import (
	"io"
	"strings"
	"testing"
)

type Game struct {
	id    int
	cubes []Rgb
}

type Rgb struct{ r, g, b int }

func parseGame(line string) Game {
	parts := strings.Split(line, ": ")
	id := requireInt(parts[0][5:])
	var cubes []Rgb
	for _, p := range strings.Split(parts[1], "; ") {
		c := Rgb{}
		for _, p2 := range strings.Split(p, ", ") {
			parts := strings.Split(p2, " ")
			count := requireInt(parts[0])
			color := parts[1]
			switch color {
			case "red":
				c.r = count
			case "blue":
				c.b = count
			case "green":
				c.g = count
			}
		}
		cubes = append(cubes, c)
	}
	return Game{id: id, cubes: cubes}
}

func validGame(game Game, rgb Rgb) bool {
	return noneMatch(game.cubes, func(cubes Rgb) bool {
		return cubes.r > rgb.r || cubes.g > rgb.g || cubes.b > rgb.b
	})
}

func countValidGames(r io.Reader) int {
	games := parseLines(r, parseGame)
	valid := filter(games, partial(validGame, Rgb{12, 13, 14}))
	return sum(map2(valid, func(g Game) int { return g.id }))
}

func minCubes(game Game) Rgb {
	r, g, b := 0, 0, 0
	for _, c := range game.cubes {
		r = max(r, c.r)
		g = max(g, c.g)
		b = max(b, c.b)
	}
	return Rgb{r, g, b}
}

func minCubesProduct(r io.Reader) int {
	games := parseLines(r, parseGame)
	products := map2(games, compose(compose(minCubes, func(rgb Rgb) []int {
		return []int{rgb.r, rgb.g, rgb.b}
	}), product))
	return sum(products)
}

func TestDay02(t *testing.T) {
	example := `
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
`
	assert(t, 8, run(countValidGames, inputString(example)))
	assert(t, 3035, run(countValidGames, inputFile(2)))

	assert(t, 2286, run(minCubesProduct, inputString(example)))
	assert(t, 66027, run(minCubesProduct, inputFile(2)))
}
