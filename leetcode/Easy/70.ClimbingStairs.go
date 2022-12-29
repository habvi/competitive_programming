package main

import (
	"fmt"
)

// TLE ---------------------------------
// func dfs(n, total int) int {
// 	if total > n {
// 		return 0
// 	}
// 	if total == n {
// 		return 1
// 	}
// 	return dfs(n, total+1) + dfs(n, total+2)
// }

// func climbStairs(n int) int {
// 	return dfs(n, 0)
// }
// -------------------------------------

// overflow ----------------------------
// func min(x, y int) int {
// 	return int(math.Min(float64(x), float64(y)))
// }

// func combinations(n, r int) uint64 {
// 	if n < r {
// 		return 0
// 	}
// 	r = min(r, n-r)
// 	var nmrt uint64 = 1
// 	var dnmnt uint64 = 1
// 	for i := 1; i <= r; i++ {
// 		nmrt = nmrt * (uint64(n) + 1 - uint64(i))
// 		dnmnt *= uint64(i)
// 		fmt.Println(nmrt, dnmnt)
// 	}
// 	return nmrt / dnmnt
// }

// func climbStairs(n int) int {
// 	var ans uint64
// 	for two := 0; two <= n/2; two++ {
// 		one := n - 2*two
// 		ans += combinations(one+two, one)
// 	}
// 	return int(ans)
// }
// -------------------------------------

func climbStairs(n int) int {
	dp := make([]int, n+1)
	dp[0] = 1
	for i := 0; i <= n; i++ {
		if i+1 <= n {
			dp[i+1] += dp[i]
		}
		if i+2 <= n {
			dp[i+2] += dp[i]
		}
	}
	return dp[n]
}

func main() {
	fmt.Println(climbStairs(45)) // 1836311903
}
