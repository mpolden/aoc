package aoc25

import (
	"bytes"
	"io"
	"slices"
	"strings"
	"testing"
)

type Range struct {
	start int
	end   int
}

func parseRanges(r io.Reader) []Range {
	var ranges []Range
	b, _ := io.ReadAll(r)
	b = bytes.TrimSpace(b)
	for s := range strings.SplitSeq(string(b), ",") {
		s = strings.TrimSpace(s)
		if s == "" {
			continue
		}
		startEnd := strings.Split(s, "-")
		start := atoi(startEnd[0])
		end := atoi(startEnd[1])
		ranges = append(ranges, Range{start: start, end: end})
	}
	return ranges
}

func sumInvalid(r io.Reader, atLeastTwice bool) int64 {
	var sum int64
	for _, rng := range parseRanges(r) {
		for n := rng.start; n <= rng.end; n++ {
			digits := digits(n)
			var groupSizes []int
			if atLeastTwice {
				for div := len(digits); div > 0; div-- {
					if len(digits)%div == 0 {
						groupSizes = append(groupSizes, len(digits)/div)
					}
				}
			} else if len(digits)%2 == 0 {
				groupSizes = append(groupSizes, len(digits)/2)
			}
			for _, size := range groupSizes {
				var (
					first       = digits[:size]
					consecutive = len(digits) > size
				)
				for i := size; i < len(digits); i += size {
					group := digits[i : i+size]
					if !slices.Equal(first, group) {
						consecutive = false
						break
					}
				}
				if consecutive {
					sum += int64(n)
					break
				}
			}
		}
	}
	return sum
}

func TestDay02(t *testing.T) {
	example := `
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124
`
	check(t, 1227775554, partial(sumInvalid, false), readString(example))
	check(t, 30608905813, partial(sumInvalid, false), readFile(2))
	check(t, 4174379265, partial(sumInvalid, true), readString(example))
	check(t, 31898925685, partial(sumInvalid, true), readFile(2))
}
