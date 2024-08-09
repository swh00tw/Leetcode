/*
 * @lc app=leetcode id=136 lang=golang
 *
 * [136] Single Number
 */

// @lc code=start
func singleNumber(nums []int) int {
	ans := 0
	for _, val := range nums {
		ans = ans ^ val
	}
	return ans

}

// @lc code=end

