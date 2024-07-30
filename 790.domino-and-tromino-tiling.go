/*
 * @lc app=leetcode id=790 lang=golang
 *
 * [790] Domino and Tromino Tiling
 */

// @lc code=start
import "math"

// ans: https://leetcode.com/problems/domino-and-tromino-tiling/?envType=study-plan-v2&envId=leetcode-75
func numTilings(n int) int {
	// for n > 3, answer comes from a few sources
	// 1. ans[n-3] * 5
	// 2. ans[n-2] * 2
	// 3. ans[n-1] * 1
	// base cases,
	// n == 1: 1
	// n == 2: 2
	// n == 3: 5
	ans := []int{1, 2, 5}
	if n <= 3 {
		return ans[n-1]
	}
	for i := 3; i < n; i++ {
		best := (ans[i-3] + ans[i-1]*2) % int(math.Pow(10, 9)+7)
		ans = append(ans, best)
	}
	return ans[len(ans)-1]
}

// @lc code=end

