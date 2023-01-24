package main

import (
	"fmt"
	"sort"
)

func findMin(nums []int) int {
	size := len(nums)
	start := sort.Search(size, func(r int) bool { return nums[0] > nums[r] })
	if start == size {
		return nums[0]
	}
	return nums[start]
}

func main() {
	nums := []int{3, 4, 5, 1, 2}
	fmt.Println(findMin(nums))

	nums = []int{4, 5, 6, 7, 0, 1, 2}
	fmt.Println(findMin(nums))

	nums = []int{11, 13, 15, 17}
	fmt.Println(findMin(nums))
}
