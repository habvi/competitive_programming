package main

import (
	"fmt"
	"math"
	"sort"
)

type Pair struct {
	Num   int
	Index int
}

type Height []Pair

func (v Height) Len() int {
	return len(v)
}

func (v Height) Less(i, j int) bool {
	return v[i].Num < v[j].Num
}

func (v Height) Swap(i, j int) {
	v[i], v[j] = v[j], v[i]
}

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
	vector := Height{}
	const INF int = 100100
	mn := INF
	mx := -INF
	var ans int

	for i := 0; i < len; i++ {
		vector = append(vector, Pair{Num: height[i], Index: i})
	}
	sort.Sort(sort.Reverse(vector))
	for i := 0; i < len; i++ {
		h, i := vector[i].Num, vector[i].Index
		if mn != INF {
			ans = max(ans, abs(i-mn)*h)
		}
		if mx != -INF {
			ans = max(ans, abs(mx-i)*h)
		}
		mn = min(mn, i)
		mx = max(mx, i)
	}
	return ans
}

func main() {
	v := []int{1, 8, 6, 2, 5, 4, 8, 3, 7}
	fmt.Println(maxArea(v))
}

// 473ms, 5.2%
