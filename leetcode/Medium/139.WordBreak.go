package main

import "fmt"

func wordBreak(s string, wordDict []string) bool {
	size := len(s)
	dp := make([]bool, size+1)
	dp[0] = true
	for i := 0; i < size+1; i++ {
		if dp[i] == false {
			continue
		}
		for _, word := range wordDict {
			len_word := len(word)
			l := i
			r := l + len_word
			if r < size+1 && s[l:r] == word {
				dp[r] = true
			}
		}
	}
	return dp[size]
}

func main() {
	s := "applepenapple"
	wordDict := []string{"pen", "apple"}
	fmt.Println(wordBreak(s, wordDict))
}
