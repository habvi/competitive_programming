package main

import (
	"fmt"
	"math"
)

func min(x, y int) int {
	return int(math.Min(float64(x), float64(y)))
}

func coinChange(coins []int, amount int) int {
	dp := make([]int, amount+1)
	const INF int = 10001
	for i := 0; i < amount+1; i++ {
		dp[i] = INF
	}
	dp[0] = 0
	for _, x := range coins {
		for i := 0; i < amount+1; i++ {
			if i+x <= amount {
				dp[i+x] = min(dp[i+x], dp[i]+1)
			}
		}
	}
	ans := dp[amount]
	if ans == INF {
		return -1
	}
	return ans
}

func main() {
	coins := []int{2, 1, 5}
	fmt.Println(coinChange(coins, 11))

	coins = []int{186, 419, 83, 408}
	fmt.Println(coinChange(coins, 6249))
}
