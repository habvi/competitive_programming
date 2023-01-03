package main

import (
	"fmt"
	"strconv"
)

func numDecodings(s string) int {
	n := len(s)
	dp := make([]int, n+1)
	if s[0] != '0' {
		dp[0] = 1
	}
	for i := 1; i <= n; i++ {
		if s[i-1] != '0' {
			x, _ := strconv.Atoi(s[i-1 : i])
			if 1 <= x && x <= 26 {
				dp[i] += dp[i-1]
			}
		}
		if i-2 >= 0 && s[i-2] != '0' {
			x, _ := strconv.Atoi(s[i-2 : i])
			if 1 <= x && x <= 26 {
				dp[i] += dp[i-2]
			}
		}
	}
	return dp[n]
}

func main() {
	s := "226"
	fmt.Println(numDecodings(s))
}
