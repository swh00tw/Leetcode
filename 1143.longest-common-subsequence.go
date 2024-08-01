/*
 * @lc app=leetcode id=1143 lang=golang
 *
 * [1143] Longest Common Subsequence
 */

// @lc code=start
package main

import "math"

func longestCommonSubsequence(text1 string, text2 string) int {
	// if text1[-1] and text[-1] the same, ans is lcs(text1[:-1], text2[:-1]) + 1
	// else, answer might be either lcs(text1[:-1], text2) or lcs(text1, text2[:-1])
	// base case: if m == 0 or n == 0, lcs is 0
	m := len(text1)
	n := len(text2)
	ans := make([][]int, m+1)
	for i, _ := range ans {
		ans[i] = make([]int, n+1)
	}

	for i := 1; i < m+1; i++ {
		for j := 1; j < n+1; j++ {
			if text1[i-1] == text2[j-1] {
				ans[i][j] = 1 + ans[i-1][j-1]
			} else {
				ans[i][j] = int(math.Max(float64(ans[i-1][j]), float64(ans[i][j-1])))
			}
		}
	}
	return ans[m][n]
}

// @lc code=end
