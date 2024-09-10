/*
 * @lc app=leetcode id=35 lang=golang
 *
 * [35] Search Insert Position
 */

// @lc code=start
package main

func searchInsert(nums []int, target int) int {
	l, r := 0, len(nums)-1
	for l <= r {
		mid := (l + r) / 2
		if nums[mid] == target {
			return mid
		}
		if nums[mid] > target {
			r = mid - 1
		} else {
			l = mid + 1
		}
	}
	return l
}

// @lc code=end
