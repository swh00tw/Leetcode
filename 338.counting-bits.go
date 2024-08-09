/*
 * @lc app=leetcode id=338 lang=golang
 *
 * [338] Counting Bits
 */

// @lc code=start
package main

func countBits(n int) []int {
	// dp
	// ones[7] (111) = 1 + ones[3] (11)
	ans := make([]int, n+1)
	ans[0] = 0
	divider := 1
	for i := 1; i <= n; i++ {
		if i == divider*2 {
			divider = divider * 2
		}
		ans[i] = 1 + ans[i%divider]
	}
	return ans
}

// @lc code=end
