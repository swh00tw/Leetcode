/*
 * @lc app=leetcode id=264 lang=golang
 *
 * [264] Ugly Number II
 */

// @lc code=start
package main

// ans: https://leetcode.com/problems/ugly-number-ii/editorial/
func nthUglyNumber(n int) int {
	nums := make([]int, n)
	nums[0] = 1
	idxBaseOf2, idxBaseOf3, idxBaseOf5 := 0, 0, 0
	nextMultipleOf2, nextMultipleOf3, nextMultipleOf5 := 2, 3, 5
	for i := 1; i < n; i++ {
		m := getMin(nextMultipleOf2, nextMultipleOf3, nextMultipleOf5)
		nums[i] = m
		if m == nextMultipleOf2 {
			idxBaseOf2++
			nextMultipleOf2 = nums[idxBaseOf2] * 2
		}
		if m == nextMultipleOf3 {
			idxBaseOf3++
			nextMultipleOf3 = nums[idxBaseOf3] * 3
		}
		if m == nextMultipleOf5 {
			idxBaseOf5++
			nextMultipleOf5 = nums[idxBaseOf5] * 5
		}
	}
	return nums[n-1]
}

func getMin(a, b, c int) int {
	if a < b {
		if a < c {
			return a
		}
		return c
	}
	if b < c {
		return b
	}
	return c
}

// @lc code=end
