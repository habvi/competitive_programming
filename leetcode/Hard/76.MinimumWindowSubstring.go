package main

import (
	"fmt"
	"math"
)

func min(x, y int) int {
	return int(math.Min(float64(x), float64(y)))
}

func calc_each_len_t(str string) map[byte]int {
	res := make(map[byte]int)
	for _, s := range str {
		res[byte(s)] += 1
	}
	return res
}

func is_same_map(nums, each_len_t map[byte]int) bool {
	ok := true
	for k, v := range each_len_t {
		if nums[k] < v {
			ok = false
			break
		}
	}
	return ok
}

func minWindow(s string, t string) string {
	nums := make(map[byte]int)
	len_s := len(s)
	min_len := 100005
	var r, ans_l, ans_r int
	each_len_t := calc_each_len_t(t)
	for l := range s {
		for r < len_s && !is_same_map(nums, each_len_t) {
			nums[s[r]] += 1
			r++
		}
		len_nums := r - l
		if is_same_map(nums, each_len_t) && len_nums < min_len {
			ans_l, ans_r = l, r
			min_len = len_nums
		}
		nums[s[l]] -= 1
		if nums[s[l]] == 0 {
			delete(nums, s[l])
		}
	}
	return s[ans_l:ans_r]
}

func main() {
	s := "ADOBECODEBANC"
	t := "ABC"
	fmt.Println(minWindow(s, t))
}
