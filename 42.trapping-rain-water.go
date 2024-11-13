/*
 * @lc app=leetcode id=42 lang=golang
 *
 * [42] Trapping Rain Water
 */

// @lc code=start
package main

import (
	"slices"
)

/*
Finds trapping intervals
*/
func trap(height []int) int {
	if len(height) <= 2 {
		return 0
	}
	var count func(height []int) []int
	count = func(height []int) []int {
		// 2 pointers
		intervals := [][]int{}
		n := len(height)
		l, r := 0, 0
		for r < n {
			if l == r {
				r++
				continue
			}
			if height[r] < height[l] {
				r++
			} else {
				interval := []int{l, r}
				if r > l+1 {
					intervals = append(intervals, interval)
				}
				l = r
			}
		}
		// count trap volume
		ans := 0
		for _, interval := range intervals {
			left := height[interval[0]]
			right := height[interval[1]]
			waterline := min(left, right)
			for i := interval[0] + 1; i < interval[1]; i++ {
				ans += waterline - height[i]
			}
		}
		return []int{ans, l}
	}
	ans1 := count(height)
	// if l not reach end, reverse the rest and keep finding intervals
	if ans1[1] != len(height)-1 {
		res := height[ans1[1]:]
		slices.Reverse(res)
		return ans1[0] + count(res)[0]
	}
	return ans1[0]
}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

// @lc code=end
