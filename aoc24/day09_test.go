package aoc24

import (
	"bufio"
	"io"
	"slices"
	"testing"
)

type extent struct {
	id    int
	start int
	end   int
	used  int
}

func (e extent) available() int {
	if e.id < 0 {
		return e.size() - e.used
	}
	return 0
}

func (e extent) size() int { return e.end - e.start + 1 }

func parseDisk(r io.Reader) []int {
	var disk []int
	s := bufio.NewReader(r)
	for i := 0; ; i++ {
		r, _, err := s.ReadRune()
		if err == io.EOF {
			break
		} else if err != nil {
			panic(err)
		}
		size := int(r - '0')
		id := -1
		if i%2 == 0 {
			id = (i / 2)
		}
		for range size {
			disk = append(disk, id)
		}
	}
	return disk
}

func compact(disk []int) {
	for i := len(disk) - 1; i >= 0; i-- {
		for j := range disk {
			if disk[i] != -1 && disk[j] == -1 {
				if i < j {
					return
				}
				disk[j], disk[i] = disk[i], disk[j]
			}
		}
	}
}

func defragment(disk []int) {
	var extents []extent
	for i := 0; i < len(disk); i++ {
		id := disk[i]
		start, end := i, i
		for j := i; j < len(disk) && disk[j] == id; j++ {
			end, i = j, j
		}
		extents = append(extents, extent{id, start, end, 0})
	}
	for _, e1 := range slices.Backward(extents) {
		if e1.id < 0 {
			continue
		}
		for i := 0; i < len(extents); i++ {
			e2 := extents[i]
			if e2.start >= e1.start {
				break
			}
			if e2.available() < e1.size() {
				continue
			}
			freeBlock := e2.start + e2.used
			for block := e1.start; block <= e1.end; block++ {
				disk[block], disk[freeBlock] = disk[freeBlock], disk[block]
				freeBlock++
				extents[i].used++
			}
			break
		}
	}
}

func findChecksum(r io.Reader, defrag bool) int {
	checksum := 0
	disk := parseDisk(r)
	if defrag {
		defragment(disk)
	} else {
		compact(disk)
	}
	for i, id := range disk {
		if id < 0 {
			continue
		}
		checksum += i * id
	}
	return checksum
}

func TestDay09(t *testing.T) {
	example := "2333133121414131402"
	check(t, 1928, partial(findChecksum, false), readString(example))
	check(t, 6201130364722, partial(findChecksum, false), readFile(9))
	check(t, 2858, partial(findChecksum, true), readString(example))
	check(t, 6221662795602, partial(findChecksum, true), readFile(9))
}
