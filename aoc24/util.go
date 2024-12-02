package aoc24

import (
	"bufio"
	"fmt"
	"io"
	"math"
	"os"
	"strconv"
	"strings"
	"testing"
)

func assert(t *testing.T, want, got int) {
	t.Helper()
	if got != want {
		t.Errorf("got %d, want %d", got, want)
	}
}

func run(f func(r io.Reader) int, r io.Reader) int {
	if rc, ok := r.(io.ReadCloser); ok {
		defer rc.Close()
	}
	return f(r)
}

func check(t *testing.T, want int, f func(r io.Reader) int, r io.Reader) {
	t.Helper()
	got := f(r)
	assert(t, want, got)
}

func inputFile(day int) *os.File {
	f, err := os.Open(fmt.Sprintf("input/input%02d.txt", day))
	if err != nil {
		panic(err)
	}
	return f
}

func inputString(s string) io.Reader { return strings.NewReader(strings.TrimSpace(s)) }

// Parsing

func lines(r io.Reader, f func(line string)) {
	scanner := bufio.NewScanner(r)
	for scanner.Scan() {
		line := strings.TrimSpace(scanner.Text())
		f(line)
	}
	if err := scanner.Err(); err != nil {
		panic(err)
	}
}

func parseLines[T any](r io.Reader, parser func(line string) T) []T {
	var values []T
	lines(r, func(line string) {
		values = append(values, parser(line))
	})
	return values
}

func atoi(s string) int {
	n, err := strconv.Atoi(s)
	if err != nil {
		panic(err)
	}
	return n
}

func runes(s string) []rune { return []rune(s) }

func isDigit(r rune) bool { return int(r) >= 48 && int(r) <= 57 }

// Functional

func partial[V1, V2, R any](f func(V1, V2) R, frozenArg V2) func(V1) R {
	return func(v1 V1) R { return f(v1, frozenArg) }
}

func compose[V1, R1, R2 any](f1 func(V1) R1, f2 func(R1) R2) func(V1) R2 {
	return func(v V1) R2 { return f2(f1(v)) }
}

func reduce[V any](values []V, f func(a, b V) V, initial V) V {
	acc := initial
	for _, v := range values {
		acc = f(acc, v)
	}
	return acc
}

// map is reserved :(
func transform[V any, R any](values []V, f func(v V) R) []R {
	result := make([]R, len(values))
	for i, v := range values {
		result[i] = f(v)
	}
	return result
}

func filter[V any](values []V, pred func(v V) bool) []V {
	var result []V
	for _, v := range values {
		if pred(v) {
			result = append(result, v)
		}
	}
	return result
}

func quantify[V any](values []V, pred func(v V) bool) int {
	n := 0
	for _, v := range values {
		if pred(v) {
			n++
		}
	}
	return n
}

func some[V any](values []V, pred func(v V) bool) bool { return quantify(values, pred) > 0 }

func all[V any](values []V, pred func(v V) bool) bool {
	return quantify(values, pred) == len(values)
}

func none[V any](values []V, pred func(v V) bool) bool { return quantify(values, pred) == 0 }

// Math

func add(a, b int) int { return a + b }

func mul(a, b int) int { return a * b }

func pow(a, b int) int { return int(math.Pow(float64(a), float64(b))) }

func product(ints []int) int { return reduce(ints, mul, 1) }

func sum(ints []int) int { return reduce(ints, add, 0) }

func abs(n int) int { return int(math.Abs(float64(n))) }

// Collections

type Set[V comparable] struct{ set map[V]bool }

func NewSet[V comparable](vs []V) *Set[V] {
	set := Set[V]{}
	set.AddAll(vs)
	return &set
}

func (s *Set[V]) Add(v V) bool {
	_, ok := s.set[v]
	if !ok {
		if s.set == nil {
			s.set = make(map[V]bool)
		}
		s.set[v] = true
	}
	return !ok
}

func (s *Set[V]) AddAll(vs []V) bool {
	changed := false
	for _, v := range vs {
		if s.Add(v) {
			changed = true
		}
	}
	return changed
}

func (s *Set[V]) Contains(v V) bool {
	_, ok := s.set[v]
	return ok
}

func (s *Set[V]) Slice() []V {
	values := make([]V, 0, len(s.set))
	for v := range s.set {
		values = append(values, v)
	}
	return values
}

func (s *Set[V]) Len() int { return len(s.set) }

func (s *Set[V]) Reset() { clear(s.set) }
