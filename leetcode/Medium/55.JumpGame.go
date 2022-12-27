package main

import (
	"fmt"
	"math"
)

func max(x, y int) int {
	return int(math.Max(float64(x), float64(y)))
}

func min(x, y int) int {
	return int(math.Min(float64(x), float64(y)))
}

// 62ms

func canJump(nums []int) bool {
	size := len(nums)
	reachable := make([]bool, size)
	reachable[0] = true

	right := 0
	for i := 0; i < size; i++ {
		if !reachable[i] {
			continue
		}
		for j := max(i, right); j < min(size, i+nums[i]+1); j++ {
			reachable[j] = true
		}
		right = min(size, max(right, i+nums[i]))
	}
	return reachable[size-1]
}

func main() {
	nums := []int{2, 3, 1, 1, 4}
	fmt.Println(canJump(nums))
}
