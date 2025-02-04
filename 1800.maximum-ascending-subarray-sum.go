/*
 * @lc app=leetcode id=1800 lang=golang
 *
 * [1800] Maximum Ascending Subarray Sum
 */

// @lc code=start
func maxAscendingSum(nums []int) int {
	ans := 0

	sum := nums[0]
	for r, n := range nums {
		if r == 0 {
			continue
		}
		if n > nums[r-1] {
			sum += n
		} else {
			if sum > ans {
				ans = sum
			}
			sum = n
		}
	}
	if sum != 0 {
		if sum > ans {
			ans = sum
		}
	}
	return ans
}

// @lc code=end

