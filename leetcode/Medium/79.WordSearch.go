package main

import "fmt"

func dfs(board [][]byte, word string, seen [][]bool, h, w, i, j, now int) bool {
	if now == len(word)-1 {
		return true
	}
	for _, d := range [][]int{{1, 0}, {0, -1}, {-1, 0}, {0, 1}} {
		dy, dx := d[0], d[1]
		ny, nx := i+dy, j+dx
		if !(0 <= ny && ny < h && 0 <= nx && nx < w) {
			continue
		}
		if seen[ny][nx] {
			continue
		}
		if board[ny][nx] == word[now+1] {
			seen[ny][nx] = true
			if dfs(board, word, seen, h, w, ny, nx, now+1) {
				return true
			}
			seen[ny][nx] = false
		}
	}
	return false
}

func exist(board [][]byte, word string) bool {
	h := len(board)
	w := len(board[0])
	for i := 0; i < h; i++ {
		for j := 0; j < w; j++ {
			if board[i][j] != word[0] {
				continue
			}
			seen := make([][]bool, h)
			for k := 0; k < h; k++ {
				seen[k] = make([]bool, w)
			}
			seen[i][j] = true
			if dfs(board, word, seen, h, w, i, j, 0) {
				return true
			}
		}
	}
	return false
}

func main() {
	board := [][]byte{{'A', 'B', 'C', 'E'}, {'S', 'F', 'C', 'S'}, {'A', 'D', 'E', 'E'}}
	word := "ABCCED"
	fmt.Println(exist(board, word))
	word = "ABCB"
	// fmt.Println(exist(board, word))
}
