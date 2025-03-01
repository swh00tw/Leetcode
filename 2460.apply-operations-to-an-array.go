/*
 * @lc app=leetcode id=2460 lang=golang
 *
 * [2460] Apply Operations to an Array
 */

// @lc code=start
package main

func applyOperations(nums []int) []int {
	n := len(nums)
	for i := 0; i < n-1; i++ {
		if nums[i] == nums[i+1] {
			nums[i] = nums[i] * 2
			nums[i+1] = 0
		}
	}
	res := make([]int, n)
	curr := 0
	for _, n := range nums {
		if n != 0 {
			res[curr] = n
			curr++
		}
	}
	return res
}

// @lc code=end
