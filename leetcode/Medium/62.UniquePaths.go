package main

import "fmt"

func uniquePaths(m int, n int) int {
	dp := make([][]int, m)
	for i := 0; i < m; i++ {
		dp[i] = make([]int, n)
	}
	dp[0][0] = 1
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if j+1 < n {
				dp[i][j+1] += dp[i][j]
			}
			if i+1 < m {
				dp[i+1][j] += dp[i][j]
			}
		}
	}
	return dp[m-1][n-1]
}

func main() {
	fmt.Println(uniquePaths(3, 7))
}
