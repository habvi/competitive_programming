package main

import "fmt"

func containsDuplicate(nums []int) bool {
	set := make(map[int]struct{})
	for _, x := range nums {
		set[x] = struct{}{}
	}
	return len(nums) != len(set)
}

func main() {
	nums := []int{1, 2, 3, 1}
	fmt.Println(containsDuplicate(nums))
}
