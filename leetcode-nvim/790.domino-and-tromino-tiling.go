package main

// @leet start
func numTilings(n int) int {
	// ref: https://leetcode.com/problems/domino-and-tromino-tiling/description/comments/1566271/
	// ans[i+1] = 2*ans[i] + ans[i-2]
	ans := []int{0, 1, 2, 5}
	if n < 4 {
		return ans[n]
	}
	for i := 4; i <= n; i++ {
		newAns := (2*ans[i-1] + ans[i-3]) % 1000000007
		ans = append(ans, newAns)
	}
	return ans[n]
}

// @leet end

