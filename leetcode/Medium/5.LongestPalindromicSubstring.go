package main

import "fmt"

func find_substr(s string, s_len int, max_len *int, start *int, left int, right int) {
	var sub_len int

	for 0 <= left && right < s_len && s[left] == s[right] {
		sub_len = right - left + 1
		if sub_len > *max_len {
			*start = left
			*max_len = sub_len
		}
		left--
		right++
	}
}

func longestPalindrome(s string) string {
	s_len := len(s)
	var start, max_len int

	for i := 0; i < s_len; i++ {
		find_substr(s, s_len, &max_len, &start, i, i)
		find_substr(s, s_len, &max_len, &start, i, i+1)
	}
	return s[start : start+max_len]
}

func main() {
	fmt.Println(longestPalindrome("babad"))
	fmt.Println(longestPalindrome("cbbd"))
}

// 6ms, 77.14%
