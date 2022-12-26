package main

import (
	"fmt"
	"math"
)

func max(x, y int) int {
	return int(math.Max(float64(x), float64(y)))
}

// 99ms

func maxSubArray(nums []int) int {
	const inf = 1001001001
	mx := 0
	ans := -inf
	for _, x := range nums {
		mx = max(mx+x, x)
		ans = max(ans, mx)
	}
	return ans
}

func main() {
	vec := []int{-2, 1, -3, 4, -1, 2, 1, -5, 4}
	fmt.Println(maxSubArray(vec))
}
