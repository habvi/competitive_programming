package main

import (
	"fmt"
	"math"
)

func lengthOfLongestSubstring(s string) int {
	size := len(s)
	st := make(map[byte]struct{})
	right := 0
	ans := 0
	for left := 0; left < size; left++ {
		for right < size {
			if _, ok := st[s[right]]; ok {
				break
			}
			st[s[right]] = struct{}{}
			right++
		}
		ans = int(math.Max(float64(ans), float64(len(st))))
		delete(st, s[left])
	}
	return ans
}

func main() {
	fmt.Println(lengthOfLongestSubstring("abcabcbb"))
}

// 21ms, 39.88%
