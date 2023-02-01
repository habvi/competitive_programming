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
	dp := make([]int, size)
	dp[0] = num[0]
	for i := 1; i < size; i++ {
		dp[i] = max(num[i], dp[i-1])
		if i-2 >= 0 {
			if i+1 == size {
				dp[i] = max(dp[i-1], dp[i-2])
				continue
			}
			dp[i] = max(dp[i-1], dp[i-2]+num[i])
		}
	}
	dp2 := make([]int, size)
	for i := 1; i < size; i++ {
		dp2[i] = max(num[i], dp2[i-1])
		if i-2 >= 0 {
			dp2[i] = max(dp2[i-1], dp2[i-2]+num[i])
		}
	}
	return max(dp[size-1], dp2[size-1])
}

func main() {
	num := []int{1, 2, 3, 1}
	fmt.Println(rob(num))

	num = []int{2, 3, 2}
	fmt.Println(rob(num))
}
