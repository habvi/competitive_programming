package main

// 10ms

func setZeroes(matrix [][]int) {
	h := len(matrix)
	w := len(matrix[0])
	zero_row := make([]bool, h)
	zero_col := make([]bool, w)
	for i := 0; i < h; i++ {
		for j := 0; j < w; j++ {
			if matrix[i][j] == 0 {
				zero_row[i] = true
				zero_col[j] = true
			}
		}
	}
	for i := 0; i < h; i++ {
		for j := 0; j < w; j++ {
			if zero_row[i] || zero_col[j] {
				matrix[i][j] = 0
			}
		}
	}
	// fmt.Println(matrix)
}

func main() {
	matrix := [][]int{{0, 1, 2, 0}, {3, 4, 5, 2}, {1, 3, 1, 5}}
	setZeroes(matrix)
}
