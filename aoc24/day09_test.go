package aoc24

import (
	"bufio"
	"fmt"
	"io"
	"testing"
)

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

func findChecksum(r io.Reader) int {
	checksum := 0
	disk := parseDisk(r)
	compact(disk)
	for i, id := range disk {
		if id < 0 {
			break
		}
		checksum += i * id
	}
	return checksum
}

func printDisk(disk []int) {
	for _, n := range disk {
		if n < 0 {
			fmt.Print(".")
		} else {
			fmt.Print(n)
		}
	}
	fmt.Println()
}

func TestDay09(t *testing.T) {
	example := "2333133121414131402"
	check(t, 1928, findChecksum, readString(example))
	check(t, 6201130364722, findChecksum, readFile(9))
}
