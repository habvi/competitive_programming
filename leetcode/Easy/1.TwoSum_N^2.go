package main

import "fmt"

func twoSum(nums []int, target int) []int {
	len := len(nums)
	ans := make([]int, 2, 2)
	for i := 0; i < len; i++ {
		for j := i + 1; j < len; j++ {
			if nums[i]+nums[j] == target {
				ans[0] = i
				ans[1] = j
				break
			}
		}
	}
	return ans
}

func main() {
	fmt.Println(twoSum([]int{2, 7, 11, 15}, 18))
}

// 41ms, 27.1%
