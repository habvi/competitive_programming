package main

import "fmt"

// pattern1
func missingNumber(nums []int) int {
	size := len(nums)
	var extra_space int
	for i := 0; i < size; i++ {
		j := nums[i]
		if j == size {
			extra_space = -1
			continue
		}
		for 0 <= j && j < size {
			tmp := nums[j]
			nums[j] = -1
			j = tmp
		}
	}

	for i := 0; i < size; i++ {
		if nums[i] >= 0 {
			return i
		}
	}
	fmt.Println(extra_space) // how golang (void)extra_space
	return size
}

// pattern2
func missingNumber2(nums []int) int {
	size := len(nums)
	var total int
	for i := 0; i < size; i++ {
		total += nums[i]
	}
	return (1+size)*size/2 - total
}

func main() {
	nums := []int{3, 0, 1}
	fmt.Println(missingNumber(nums))
	nums = []int{9, 6, 4, 2, 3, 5, 7, 0, 1}
	fmt.Println(missingNumber(nums))
	nums = []int{1, 2}
	fmt.Println(missingNumber(nums))

	nums = []int{3, 0, 1}
	fmt.Println(missingNumber2(nums))
	nums = []int{9, 6, 4, 2, 3, 5, 7, 0, 1}
	fmt.Println(missingNumber2(nums))
	nums = []int{1, 2}
	fmt.Println(missingNumber2(nums))
}
