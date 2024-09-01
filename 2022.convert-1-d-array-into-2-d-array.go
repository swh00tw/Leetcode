/*
 * @lc app=leetcode id=2022 lang=golang
 *
 * [2022] Convert 1D Array Into 2D Array
 */

// @lc code=start
func construct2DArray(original []int, m int, n int) [][]int {
	if m*n != len(original) {
		return [][]int{}
	}
	matrix := make([][]int, m)
	for i := 0; i < m; i++ {
		matrix[i] = make([]int, n)
	}
	for i := 0; i < len(original); i++ {
		x := i / n
		y := i % n
		matrix[x][y] = original[i]
	}
	return matrix
}

// @lc code=end

