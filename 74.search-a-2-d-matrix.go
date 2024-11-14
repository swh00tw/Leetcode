/*
 * @lc app=leetcode id=74 lang=golang
 *
 * [74] Search a 2D Matrix
 */

// @lc code=start
package main

/*
1. find which row -> binary search to find the right most item that is lower or equal than target
2. find if the number is presented in that row
*/
func searchMatrix(matrix [][]int, target int) bool {
	n := len(matrix)
	l, r := 0, n-1
	for l <= r {
		m := (l + r) / 2
		if matrix[m][0] == target {
			return true
		}
		if matrix[m][0] < target {
			l = m + 1
		} else {
			r = m - 1
		}
	}
	if r == -1 {
		return false
	}
	row := matrix[r]
	m := len(row)
	l, r = 0, m-1
	for l <= r {
		m := (l + r) / 2
		if row[m] == target {
			return true
		}
		if row[m] < target {
			l = m + 1
		} else {
			r = m - 1
		}
	}
	return false
}

// @lc code=end
