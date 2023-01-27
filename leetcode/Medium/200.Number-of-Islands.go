package main

import (
	"container/list"
	"fmt"
)

func PopFrontDeque(deque *list.List) interface{} {
	x := deque.Front()
	if x == nil {
		return nil
	}
	return deque.Remove(x)
}

func bfs(grid [][]byte, seen [][]bool, h, w, sy, sx int) [][]bool {
	q := list.New()
	q.PushBack([]int{sy, sx})
	seen[sy][sx] = true
	for q.Len() > 0 {
		xy := PopFrontDeque(q)
		y, x := xy.([]int)[0], xy.([]int)[1]
		for _, dxy := range [][]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}} {
			ny, nx := dxy[0]+y, dxy[1]+x
			if !(0 <= ny && ny < h && 0 <= nx && nx < w) || grid[ny][nx] == '0' {
				continue
			}
			if seen[ny][nx] == true {
				continue
			}
			seen[ny][nx] = true
			q.PushBack([]int{ny, nx})
		}
	}
	return seen
}

func numIslands(grid [][]byte) int {
	h := len(grid)
	w := len(grid[0])
	seen := make([][]bool, h)
	for i := 0; i < h; i++ {
		seen[i] = make([]bool, w)
	}
	var ans int
	for y := 0; y < h; y++ {
		for x := 0; x < w; x++ {
			if seen[y][x] == false && grid[y][x] == '1' {
				seen = bfs(grid, seen, h, w, y, x)
				ans++
			}
		}
	}
	return ans
}

func main() {
	grid := [][]byte{{'1', '1', '0'}, {'1', '1', '0'}, {'0', '0', '1'}, {'0', '0', '1'}}
	fmt.Println(numIslands(grid))
}
