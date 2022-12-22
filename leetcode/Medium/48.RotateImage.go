package main

func rotate(matrix [][]int) {
	n := len(matrix)
	for i := 0; i < n; i++ {
		for j := i; j < n-i-1; j++ {
			var tmp [4]int
			tmp[0] = matrix[i][j]
			tmp[1] = matrix[j][n-i-1]
			tmp[2] = matrix[n-i-1][n-j-1]
			tmp[3] = matrix[n-j-1][i]

			matrix[j][n-i-1] = tmp[0]
			matrix[n-i-1][n-j-1] = tmp[1]
			matrix[n-j-1][i] = tmp[2]
			matrix[i][j] = tmp[3]
		}
	}
}
