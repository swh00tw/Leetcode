/*
 * @lc app=leetcode id=2419 lang=golang
 *
 * [2419] Longest Subarray With Maximum Bitwise AND
 */

// @lc code=start
package main

import "fmt"

/*
Maintain 2 pointers: l, r
keep moving r until AND become lower, update best answer
if AND become lower, reset l to r
*/
func longestSubarray(nums []int) int {
	n := len(nums)
	l, r := 0, 0
	and := nums[0]
	best := []int{-1, 0} // [k, length of subarray]
	for r < n-1 {
		r++
		nextAnd := and & nums[r]
		if nums[r] < nextAnd && nextAnd >= best[0] {
			and = nextAnd
			fmt.Println(l, r, and)
			best = []int{and, r + 1 - l}
		} else {
			l = r
			fmt.Println("move left to ", l)
			and = nums[r]
		}
	}
	return best[1]
}

// @lc code=end
