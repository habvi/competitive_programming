package main

import (
	"fmt"
	"math"
)

func max(x, y int) int {
	return int(math.Max(float64(x), float64(y)))
}

func rob(num []int) int {
	size := len(num)
	dp := make([]int, size+1)
	for i := 1; i < size+1; i++ {
		if i-1 >= 0 {
			dp[i] = max(num[i-1], dp[i-1])
		}
		if i-2 >= 0 {
			dp[i] = max(dp[i], dp[i-2]+num[i-1])
		}
	}
	return dp[size]
}

func main() {
	num := []int{2, 7, 9, 3, 1}
	fmt.Println(rob(num))
}
