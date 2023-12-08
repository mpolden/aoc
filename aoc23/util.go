package aoc23

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
	"testing"
)

type Set[V comparable] struct{ set map[V]bool }

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

func partial[V1, V2, R any](f func(V1, V2) R, frozenArg V2) func(V1) R {
	return func(v1 V1) R { return f(v1, frozenArg) }
}

func compose[V1, R1, R2 any](f1 func(V1) R1, f2 func(R1) R2) func(V1) R2 {
	return func(v V1) R2 { return f2(f1(v)) }
}

func parseLines[T any](r io.Reader, parser func(line string) T) []T {
	scanner := bufio.NewScanner(r)
	var values []T
	for scanner.Scan() {
		line := strings.TrimSpace(scanner.Text())
		values = append(values, parser(line))
	}
	return values
}

func inputFile(day int) *os.File {
	f, err := os.Open(fmt.Sprintf("input/input%02d.txt", day))
	if err != nil {
		panic(err)
	}
	return f
}

func inputString(s string) io.Reader { return strings.NewReader(strings.TrimSpace(s)) }

func requireInt(s string) int {
	n, err := strconv.Atoi(s)
	if err != nil {
		panic(err)
	}
	return n
}

func runes(s string) []rune { return []rune(s) }

func isDigit(r rune) bool { return int(r) >= 48 && int(r) <= 57 }

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func add(a, b int) int { return a + b }

func mul(a, b int) int { return a * b }

func reduce[V any](values []V, f func(a, b V) V, initial V) V {
	acc := initial
	for _, v := range values {
		acc = f(acc, v)
	}
	return acc
}

func map2[V any, R any](values []V, f func(v V) R) []R {
	mapped := make([]R, len(values))
	for i, v := range values {
		mapped[i] = f(v)
	}
	return mapped
}

func filter[V any](values []V, pred func(v V) bool) []V {
	var filtered []V
	for _, v := range values {
		if pred(v) {
			filtered = append(filtered, v)
		}
	}
	return filtered
}

func frequency[V any](values []V, pred func(v V) bool) int { return len(filter(values, pred)) }

func anyMatch[V any](values []V, pred func(v V) bool) bool { return frequency(values, pred) > 0 }

func allMatch[V any](values []V, pred func(v V) bool) bool {
	return frequency(values, pred) == len(values)
}

func noneMatch[V any](values []V, pred func(v V) bool) bool { return !anyMatch(values, pred) }

func product(ints []int) int { return reduce(ints, mul, 1) }

func sum(ints []int) int { return reduce(ints, add, 0) }
