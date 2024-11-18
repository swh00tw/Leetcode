/*
 * @lc app=leetcode id=1652 lang=golang
 *
 * [1652] Defuse the Bomb
 */

// @lc code=start
package main

import "slices"

func decrypt(code []int, k int) []int {
	if k < 0 {
		slices.Reverse(code)
		res := decrypt(code, -k)
		slices.Reverse(res)
		return res
	}
	if k == 0 {
		return make([]int, len(code))
	}
	// if k > 0
	sum := 0
	for _, v := range code {
		sum += v
	}
	n := len(code)
	round := k / n
	k = k % n

	res := make([]int, n)
	for i, _ := range code {
		res[i] = round * sum
	}
	nextK := 0
	for i := 0; i < k; i++ {
		idx := i + 1
		nextK += code[idx%n]
	}
	for i, _ := range code {
		res[i] += nextK
		// update nextK
		nextK -= code[(i+1)%n]
		nextK += code[(i+k+1)%n]
	}
	return res
}

// @lc code=end
