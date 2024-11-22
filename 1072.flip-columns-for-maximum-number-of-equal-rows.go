/*
 * @lc app=leetcode id=1072 lang=golang
 *
 * [1072] Flip Columns For Maximum Number of Equal Rows
 */

// @lc code=start
package main

/*
Just count how many rows have the same pattern
the same pattern: 001 and 110 have the same pattern
*/
func maxEqualRowsAfterFlips(matrix [][]int) int {
	patterns := make(map[string]int)
	for _, row := range matrix {
		pattern := row2Pattern(row)
		patterns[pattern]++
	}

	ans := 0
	for _, p := range patterns {
		if p > ans {
			ans = p
		}
	}
	return ans
}

func row2Pattern(row []int) string {
	bytes := make([]byte, len(row))
	for i, v := range row {
		if v == row[0] {
			bytes[i] = '0'
		} else {
			bytes[i] = '1'
		}
	}
	return string(bytes)
}

// @lc code=end
