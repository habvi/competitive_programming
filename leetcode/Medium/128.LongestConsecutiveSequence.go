package main

import (
	"fmt"
	"math"
	"sort"
)

func max(x, y int) int {
	return int(math.Max(float64(x), float64(y)))
}

func longestConsecutive(nums []int) int {
	set := make(map[int]struct{})
	for _, x := range nums {
		set[x] = struct{}{}
	}

	var list []int
	for k, _ := range set {
		list = append(list, k)
	}
	sort.Sort(sort.IntSlice(list))

	var longest, ans int
	for i := 0; i < len(list)-1; i++ {
		if list[i]+1 != list[i+1] {
			ans = max(ans, longest+1)
			longest = 0
		} else {
			longest++
		}
	}
	if len(nums) != 0 {
		ans = max(ans, longest+1)
	}
	return ans
}

func main() {
	nums := []int{100, 4, 100, 200, 1, 3, 2}
	fmt.Println(longestConsecutive(nums))
}
