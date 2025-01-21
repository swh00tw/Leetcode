/*
 * @lc app=leetcode id=2017 lang=golang
 *
 * [2017] Grid Game
 */

// @lc code=start
package main

import (
	"slices"
)

func gridGame(grid [][]int) int64 {
	n := len(grid[0])
	prefix := make([]int, n)
	suffix := make([]int, n)
	curr := 0
	for i, num := range grid[0] {
		curr += num
		prefix[i] = curr
	}
	curr = 0
	for i := n - 1; i >= 0; i-- {
		curr += grid[1][i]
		suffix[i] = curr
	}

	ans := []int64{}
	for turn := 0; turn < len(grid[0]); turn++ {
		score := Max(prefix[n-1]-prefix[turn], suffix[0]-suffix[turn])
		ans = append(ans, int64(score))
	}
	return slices.Min(ans)
}

func Max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

// @lc code=end
