package main

import "fmt"

func twoSum(nums []int, target int) []int {
	len := len(nums)

	seen := make(map[int]int)
	ans := make([]int, 2, 2)
	for i := 0; i < len; i++ {
		x := target - nums[i]
		if v, ok := seen[x]; ok {
			ans[0] = v
			ans[1] = i
			break
		}
		seen[nums[i]] = i
	}
	return ans
}

func main() {
	fmt.Println(twoSum([]int{2, 7, 11, 15}, 18))
}

// 18ms, 43.66%
