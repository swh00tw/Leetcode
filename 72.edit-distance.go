/*
 * @lc app=leetcode id=72 lang=golang
 *
 * [72] Edit Distance
 */

// @lc code=start
package main

import "math"

func minDistance(word1 string, word2 string) int {
	/*
	  # The concept is alike as the Longest Common Substring problem
	  # use bottom up DP, the goal is to find minDistance[m,n] (m = len(x), n = len(y))
	  # (minDistance[i, j] is minDistance between x[:i] and y[:j])
	  # Optimal substructure:
	  # minDistamce[i,j] = minDistance[i-1, j-1] if xi == yj
	  # else, minDistance[i,j] = min(
	  #                           minDistance[i - 1][j] + 1,       # delete
	  #                           minDistance[i][j - 1] + 1,       # insert
	  #                           minDistance[i - 1][j - 1] + 1    # replace
	  #                           )
	*/

	m := len(word1)
	n := len(word2)
	ans := make([][]int, m+1)
	for i, _ := range ans {
		ans[i] = make([]int, n+1)
	}
	// init base case
	for i := 0; i < m+1; i++ {
		ans[i][0] = i
	}
	for i := 0; i < n+1; i++ {
		ans[0][i] = i
	}
	// bottom up
	for i := 1; i < m+1; i++ {
		for j := 1; j < n+1; j++ {
			if word1[i-1] == word2[j-1] {
				ans[i][j] = ans[i-1][j-1]
			} else {
				ans[i][j] = min(ans[i-1][j]+1, ans[i][j-1]+1, ans[i-1][j-1]+1)
			}
		}
	}
	return ans[m][n]
}

func min(nums ...int) int {
	var ans int
	n := len(nums)
	if n == 0 {
		return ans
	} else if n == 1 {
		return nums[0]
	} else {
		ans = nums[0]
		for i := 1; i < n; i++ {
			ans = int(math.Min(float64(ans), float64(nums[i])))
		}
		return ans
	}
}

// @lc code=end
