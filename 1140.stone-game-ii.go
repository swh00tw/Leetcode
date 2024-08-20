/*
 * @lc app=leetcode id=1140 lang=golang
 *
 * [1140] Stone Game II
 */

// @lc code=start
package main

import "fmt"

func toString(key []int) string {
	return fmt.Sprintf("%d,%d", key[0], key[1])
}

func stoneGameII(piles []int) int {
	n := len(piles)
	suffixSum := make([]int, n+1)
	sum := 0
	for i := n - 1; i >= 0; i-- {
		sum += piles[i]
		suffixSum[i] = sum
	}
	suffixSum[n] = 0

	/* cache */
	cache := make(map[string]int)

	/* top down dp*/
	var getBestAns func(m int, startIdx int) int
	getBestAns = func(m int, startIdx int) int {
		// look up cache
		key := toString([]int{m, startIdx})
		if val, ok := cache[key]; ok {
			return val
		}
		// base case
		if startIdx >= n {
			return 0
		}
		best := 0
		for i := 1; i <= 2*m; i++ {
			if startIdx+i > n {
				break
			}
			thisRound := suffixSum[startIdx] - suffixSum[startIdx+i]
			restStones := suffixSum[startIdx+i]
			restRound := restStones - getBestAns(_max(m, i), startIdx+i)
			best = _max(best, thisRound+restRound)
		}

		// update cache
		cache[toString([]int{m, startIdx})] = best
		return best
	}

	return getBestAns(1, 0)
}

func _min(x, y int) int {
	if x <= y {
		return x
	}
	return y
}

func _max(x, y int) int {
	if x >= y {
		return x
	}
	return y
}

// @lc code=end
