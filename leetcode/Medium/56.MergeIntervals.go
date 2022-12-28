package main

import (
	"fmt"
	"math"
	"sort"
)

func max(x, y int) int {
	return int(math.Max(float64(x), float64(y)))
}

// 19ms

func merge(intervals [][]int) [][]int {
	res := [][]int{}
	sort.Slice(intervals, func(i, j int) bool { return intervals[i][0] < intervals[j][0] })
	left, right := intervals[0][0], intervals[0][1]
	intervals = append(intervals, []int{10010, 10010})
	for _, v := range intervals {
		l, r := v[0], v[1]
		if l <= right {
			right = max(right, r)
		} else {
			res = append(res, []int{left, right})
			left, right = l, r
		}
	}
	return res
}

func main() {
	vec := [][]int{{1, 3}, {8, 10}, {2, 6}, {15, 18}}
	fmt.Println(merge(vec))

	vec = [][]int{{1, 4}, {2, 3}}
	fmt.Println(merge(vec))
}
