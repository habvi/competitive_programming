package main

import (
	"fmt"
	"strconv"
)

func reverseBits(num uint32) uint32 {
	var digits [32]uint32
	for i := 0; i < 32; i++ {
		digits[i] = num % 2
		num /= 2
	}

	var res uint32
	for _, d := range digits {
		res = res*2 + d
	}
	return res
}

func main() {
	i2, _ := strconv.ParseInt("00000010100101000001111010011100", 2, 0)
	fmt.Println(reverseBits(uint32(i2)))
}
