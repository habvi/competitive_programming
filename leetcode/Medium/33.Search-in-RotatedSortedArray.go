package main

import (
	"fmt"
	"math"
	"sort"
)

// 4ms

func abs(x int) int {
	return int(math.Abs(float64(x)))
}

func is_ok(nums *[]int, right int) bool {
	return (*nums)[0] > (*nums)[right]
}

func bisect(nums *[]int, ng, ok int) int {
	for abs(ok-ng) > 1 {
		middle := (ok + ng) / 2
		if is_ok(nums, middle) {
			ok = middle
		} else {
			ng = middle
		}
	}
	return ok
}

func search(nums []int, target int) int {
	length := len(nums)
	start := bisect(&nums, -1, length)
	i := sort.Search(start, func(i int) bool { return nums[i] >= target })
	if i < start && nums[i] == target {
		return i
	}
	i = sort.Search(len(nums)-start, func(i int) bool { return nums[start+i] >= target })
	if i < len(nums)-start && nums[start+i] == target {
		return start + i
	}
	return 0
}

func main() {
	nums := []int{4, 5, 6, 7, 0, 1, 2}
	fmt.Println(search(nums, 4))
}
