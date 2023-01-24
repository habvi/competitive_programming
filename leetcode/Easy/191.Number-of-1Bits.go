package main

import (
	"fmt"
	"strconv"
)

func hammingWeight(num uint32) int {
	res := 0
	for i := 0; i < 32; i++ {
		if num%2 == 1 {
			res++
		}
		num /= 2
	}
	return res
}

func main() {
	i2, _ := strconv.ParseInt("00000010100101000001111010011100", 2, 0)
	fmt.Println(hammingWeight(uint32(i2)))
}
