package main

import (
	"fmt"
	"sort"
)

// 4sms

func search(nums []int, target int) int {
	length := len(nums)
	start := sort.Search(length, func(r int) bool { return nums[0] > nums[r] })
	idx := sort.Search(start, func(i int) bool { return nums[i] >= target })
	if idx < start && nums[idx] == target {
		return idx
	}
	length -= start
	idx = sort.Search(length, func(i int) bool { return nums[start+i] >= target })
	if idx < length && nums[start+idx] == target {
		return start + idx
	}
	return -1
}

func main() {
	nums := []int{4, 5, 6, 7, 0, 1, 2}
	fmt.Println(search(nums, 4))
}
