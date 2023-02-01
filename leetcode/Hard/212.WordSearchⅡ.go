package main

import (
	"fmt"
)

func dfs(board [][]byte, set map[string]struct{}, ans *[]string, i, j, h, w int, now string, seen [][]bool) {
	if len(now) >= 11 {
		return
	}
	if _, ok := set[now]; ok {
		*ans = append(*ans, now)
		delete(set, now)
	}
	for _, d := range [][]int{{0, 1}, {1, 0}, {-1, 0}, {0, -1}} {
		ni, nj := i+d[0], j+d[1]
		if !(0 <= ni && ni < h && 0 <= nj && nj < w) || seen[ni][nj] == true {
			continue
		}
		seen[ni][nj] = true
		dfs(board, set, ans, ni, nj, h, w, now+string(board[ni][nj]), seen)
		seen[ni][nj] = false
	}
}

func findWords(board [][]byte, words []string) []string {
	h := len(board)
	w := len(board[0])
	set := make(map[string]struct{})
	for _, word := range words {
		set[word] = struct{}{}
	}
	var ans []string
	for i := 0; i < h; i++ {
		for j := 0; j < w; j++ {
			seen := make([][]bool, h)
			for i := 0; i < h; i++ {
				seen[i] = make([]bool, w)
			}
			seen[i][j] = true
			dfs(board, set, &ans, i, j, h, w, string(board[i][j]), seen)
		}
	}
	return ans
}

func main() {
	board := [][]byte{{'o', 'a', 'a', 'n'},
		{'e', 't', 'a', 'e'},
		{'i', 'h', 'k', 'r'},
		{'i', 'f', 'l', 'v'}}
	words := []string{"oath", "pea", "eat", "rain"}
	fmt.Println(findWords(board, words))

	board = [][]byte{{'o', 'a', 'b', 'n'},
		{'a', 't', 'a', 'e'},
		{'a', 'h', 'k', 'r'},
		{'a', 'f', 'l', 'v'}}
	words = []string{"oa", "oaa"}
	fmt.Println(findWords(board, words))
}
