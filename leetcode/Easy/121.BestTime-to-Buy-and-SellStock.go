package main

import (
	"fmt"
	"math"
)

func min(x, y int) int {
	return int(math.Min(float64(x), float64(y)))
}

func max(x, y int) int {
	return int(math.Max(float64(x), float64(y)))
}

func maxProfit(prices []int) int {
	ans := 0
	const inf = 10005
	mn := inf
	for _, x := range prices {
		if mn < x {
			ans = max(ans, x-mn)
		}
		mn = min(mn, x)
	}
	return ans
}

func main() {
	vec := []int{7, 1, 5, 3, 6, 4}
	fmt.Println(maxProfit(vec))
}
