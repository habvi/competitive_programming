package main

import (
	"fmt"
	"sort"
)

func lengthOfLIS(nums []int) int {
	var lis []int
	lis = append(lis, -10001)
	for _, x := range nums {
		n := len(lis)
		idx := sort.Search(n, func(i int) bool { return lis[i] >= x })
		if lis[n-1] < x {
			lis = append(lis, x)
		} else {
			lis[idx] = x
		}
	}
	return len(lis) - 1
}

func main() {
	nums := []int{10, 9, 2, 5, 3, 7, 101, 18}
	fmt.Println(lengthOfLIS(nums))

	nums = []int{0, 1, 0, 3, 2, 3}
	fmt.Println(lengthOfLIS(nums))
}
