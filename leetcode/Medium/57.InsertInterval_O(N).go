package main

import (
	"fmt"
	"math"
	"sort"
)

func max(x, y int) int {
	return int(math.Max(float64(x), float64(y)))
}

func merge(intervals [][]int, newInterval []int, idx int) [][]int {
	res := [][]int{}
	var left, right int
	if idx == 0 {
		left, right = newInterval[0], newInterval[1]
	} else {
		left, right = intervals[0][0], intervals[0][1]
	}
	intervals = append(intervals, []int{100010, 100010})
	for i, v := range intervals {
		if i > 0 && i == idx {
			l, r := newInterval[0], newInterval[1]
			if l <= right {
				right = max(right, r)
			} else {
				res = append(res, []int{left, right})
				left, right = l, r
			}
		}
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
	size := len(intervals)
	if size == 0 {
		return [][]int{newInterval}
	}
	target := newInterval[0]
	idx := sort.Search(size, func(i int) bool { return intervals[i][0] >= target })
	return merge(intervals, newInterval, idx)
}

func main() {
	intervals := [][]int{{1, 3}, {6, 9}}
	newInterval := []int{2, 5}
	fmt.Println(insert(intervals, newInterval))

	intervals = [][]int{{1, 2}, {3, 5}, {6, 7}, {8, 10}, {12, 16}}
	newInterval = []int{4, 8}
	fmt.Println(insert(intervals, newInterval))

	intervals = [][]int{}
	newInterval = []int{5, 7}
	fmt.Println(insert(intervals, newInterval))
}
