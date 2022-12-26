package main

import (
	"fmt"
	"sort"
	"strings"
)

// 26ms

func groupAnagrams(strs []string) [][]string {
	mp := make(map[string][]string)
	for _, s := range strs {
		tmp := strings.Split(s, "")
		sort.Strings(tmp)
		sorted_s := strings.Join(tmp, "")
		mp[sorted_s] = append(mp[sorted_s], s)
	}

	var res [][]string
	for _, vec := range mp {
		res = append(res, vec)
	}
	return res
}

func main() {
	vec := []string{"eat", "tea", "tan", "ate", "nat", "bat"}
	fmt.Println(groupAnagrams(vec))
}
