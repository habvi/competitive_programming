package main

import "fmt"

func productExceptSelf(nums []int) []int {
	size := len(nums)

	from_left := make([]int, size+1)
	from_left[0] = 1
	for i := 1; i < size+1; i++ {
		from_left[i] = from_left[i-1] * nums[i-1]
	}

	from_right := make([]int, size+1)
	from_right[size] = 1
	for i := size - 1; i >= 0; i-- {
		from_right[i] = from_right[i+1] * nums[i]
	}

	ans := make([]int, size)
	for i := 0; i < size; i++ {
		ans[i] = from_left[i] * from_right[i+1]
	}
	return ans
}

/*
   1  2  3  4
1  1  2  6  24
   24 24 12  4 1
*/

func main() {
	nums := []int{1, 2, 3, 4}
	fmt.Println(productExceptSelf(nums))

	nums = []int{-1, 1, 0, -3, 3}
	fmt.Println(productExceptSelf(nums))
}
