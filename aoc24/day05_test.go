package aoc24

import (
	"io"
	"slices"
	"strings"
	"testing"
)

type rule struct{ a, b int }

type protocol struct {
	Rules   []rule
	Updates [][]int
}

func (p *protocol) rulesOf(update []int) []rule {
	var rules []rule
	for _, r := range p.Rules {
		var a, b bool
		for _, u := range update {
			if u == r.a {
				a = true
			} else if u == r.b {
				b = true
			}
		}
		if a && b {
			rules = append(rules, r)
		}
	}
	return rules
}

func (p *protocol) before(n int, update []int) []int {
	var before []int
	for _, r := range p.rulesOf(update) {
		if r.b == n {
			before = append(before, r.a)
		}
	}
	return before
}

func (p *protocol) isSorted(update []int) bool {
	for i, a := range update {
		before := p.before(a, update)
		for _, b := range update[i+1:] {
			if slices.Contains(before, b) {
				return false
			}
		}
	}
	return true
}

func (p *protocol) sort(update []int) []int {
	sorted := make([]int, len(update))
	for _, a := range update {
		before := p.before(a, update)
		i := len(before)
		sorted[i] = a
	}
	return sorted
}

func parseProtocol(r io.Reader) protocol {
	p := protocol{}
	parsingRules := true
	lines(r, func(line string) {
		if len(line) == 0 {
			parsingRules = false
		} else if parsingRules {
			parts := strings.SplitN(line, "|", 2)
			p.Rules = append(p.Rules, rule{a: atoi(parts[0]), b: atoi(parts[1])})
		} else {
			parts := strings.Split(line, ",")
			update := transform(parts, atoi)
			p.Updates = append(p.Updates, update)
		}
	})
	return p
}

func sumUpdates(r io.Reader, sort bool) int {
	sum := 0
	p := parseProtocol(r)
	for _, update := range p.Updates {
		if sort {
			if !p.isSorted(update) {
				sorted := p.sort(update)
				sum += sorted[(len(sorted)-1)/2]
			}
		} else if p.isSorted(update) {
			sum += update[(len(update)-1)/2]
		}
	}
	return sum
}

func TestDay05(t *testing.T) {
	example := `
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
`
	check(t, 143, partial(sumUpdates, false), readString(example))
	check(t, 5108, partial(sumUpdates, false), readFile(5))
	check(t, 123, partial(sumUpdates, true), readString(example))
	check(t, 7380, partial(sumUpdates, true), readFile(5))
}
