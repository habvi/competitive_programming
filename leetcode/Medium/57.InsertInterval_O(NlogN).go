package main

import (
	"fmt"
	"math"
	"sort"
)

func max(x, y int) int {
	return int(math.Max(float64(x), float64(y)))
}

// 56.MergeIntervals
func merge(intervals [][]int) [][]int {
	res := [][]int{}
	sort.Slice(intervals, func(i, j int) bool { return intervals[i][0] < intervals[j][0] })
	left, right := intervals[0][0], intervals[0][1]
	intervals = append(intervals, []int{100010, 100010})
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

// 7ms

func insert(intervals [][]int, newInterval []int) [][]int {
	intervals = append(intervals, newInterval)
	return merge(intervals)
}

func main() {
	intervals := [][]int{{1, 3}, {6, 9}}
	newInterval := []int{2, 5}
	fmt.Println(insert(intervals, newInterval))
}
