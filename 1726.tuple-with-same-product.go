/*
 * @lc app=leetcode id=1726 lang=golang
 *
 * [1726] Tuple with Same Product
 */

// @lc code=start
package main

import (
	"slices"
)

/*
1. brute force O(n^4)
2. two pointer O(n^3)
  - sort first
  - for each (l, r), find between them if any pair's product equal to nums[l]*nums[r], if found, count += 8
  - how to find? 2 pointers problem
*/
func tupleSameProduct(nums []int) int {
	ans := 0
	slices.Sort(nums)
	n := len(nums)
	for l := 0; l < n-3; l++ {
		for r := l + 3; r < n; r++ {
			p := nums[l] * nums[r]
			x := l + 1
			y := r - 1
			for x < y {
				if nums[x]*nums[y] == p {
					ans += 8
					x++
					y--
					continue
				}
				if nums[x]*nums[y] < p {
					x++
				} else {
					y--
				}
			}
		}
	}
	return ans
}

// @lc code=end
