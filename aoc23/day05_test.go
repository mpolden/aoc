package aoc23

import (
	"fmt"
	"io"
	"math"
	"strings"
	"testing"
)

type Almanac struct {
	seeds    []Range
	mappings [][]Mapping
}

func (a *Almanac) Resolve(n int) int {
	for _, rs := range a.mappings {
		for _, r := range rs {
			if found, ok := r.Target(n); ok {
				n = found
				break
			}
		}
	}
	return n
}

type Mapping struct {
	src  int
	dst  int
	size int
}

func (r Mapping) Target(n int) (int, bool) {
	if n >= r.src && n <= r.src+r.size {
		return r.dst + (n - r.src), true
	}
	return 0, false
}

type Range struct{ start, end int }

func (r Range) Each(f func(int)) {
	for i := r.start; i <= r.end; i++ {
		f(i)
	}
}

func parseMapping(s string) Mapping {
	parts := strings.Fields(s)
	if got, want := len(parts), 3; got != want {
		panic(fmt.Sprintf("got %d fields in %q, want %d", got, s, want))
	}
	ints := transform(parts, atoi)
	return Mapping{src: ints[1], dst: ints[0], size: ints[2]}
}

func parseAlmanac(r io.Reader, seedRange bool) Almanac {
	var (
		seeds    []Range
		mappings [][]Mapping
	)
	mappingIdx := -1
	parseLines(r, func(line string) string {
		if strings.HasPrefix(line, "seeds:") {
			parts := strings.Fields(line)
			ints := transform(parts[1:], atoi)
			if seedRange {
				for i := 0; i < len(ints); i += 2 {
					start := ints[i]
					end := start + ints[i+1]
					seeds = append(seeds, Range{start, end})
				}
			} else {
				for _, seed := range ints {
					seeds = append(seeds, Range{seed, seed})
				}
			}
		} else if strings.HasSuffix(line, "map:") {
			mappings = append(mappings, []Mapping{})
			mappingIdx++
		} else if mappingIdx > -1 && line != "" {
			mappings[mappingIdx] = append(mappings[mappingIdx], parseMapping(line))
		}
		return ""
	})
	return Almanac{seeds, mappings}
}

func locationNumber(r io.Reader, seedRange bool) int {
	a := parseAlmanac(r, seedRange)
	best := math.MaxInt
	for _, seed := range a.seeds {
		seed.Each(func(n int) {
			best = min(best, a.Resolve(n))
		})
	}
	return best
}

func TestDay05(t *testing.T) {
	example := `
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
`
	assert(t, 35, run(partial(locationNumber, false), inputString(example)))
	assert(t, 424490994, run(partial(locationNumber, false), inputFile(5)))

	assert(t, 46, run(partial(locationNumber, true), inputString(example)))
	assert(t, 15290096, run(partial(locationNumber, true), inputFile(5))) // Correct, but terribly slow
}
