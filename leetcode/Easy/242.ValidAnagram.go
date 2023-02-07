package main

import (
	"fmt"
	"sort"
	"strings"
)

func sort_string(s string) string {
	tmp := strings.Split(s, "")
	sort.Strings(tmp)
	sorted_s := strings.Join(tmp, "")
	return sorted_s
}

func isAnagram(s string, t string) bool {
	return sort_string(s) == sort_string(t)
}

func main() {
	s := "anagram"
	t := "nagaram"
	fmt.Println(isAnagram(s, t))
}
