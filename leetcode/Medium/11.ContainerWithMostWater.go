package main

import (
	"fmt"
	"math"
	"sort"
)

func min(x, y int) int {
	return int(math.Min(float64(x), float64(y)))
}

func max(x, y int) int {
	return int(math.Max(float64(x), float64(y)))
}
func abs(x int) int {
	return int(math.Abs(float64(x)))
}

func maxArea(height []int) int {
	len := len(height)
	vector := [][2]int{}
	const INF int = 100100
	mn, mx := INF, -INF
	var ans int

	for i := 0; i < len; i++ {
		vector = append(vector, [2]int{height[i], i})
	}
	sort.Slice(vector, func(i, j int) bool { return vector[i][0] > vector[j][0] })
	for i := 0; i < len; i++ {
		h, idx := vector[i][0], vector[i][1]
		if mn != INF {
			ans = max(ans, abs(idx-mn)*h)
		}
		if mx != -INF {
			ans = max(ans, abs(mx-idx)*h)
		}
		mn = min(mn, idx)
		mx = max(mx, idx)
	}
	return ans
}

func main() {
	v := []int{1, 8, 6, 2, 5, 4, 8, 3, 7}
	fmt.Println(maxArea(v))
}

// 258ms
