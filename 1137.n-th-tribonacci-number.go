/*
 * @lc app=leetcode id=1137 lang=golang
 *
 * [1137] N-th Tribonacci Number
 */

// @lc code=start
func tribonacci(n int) int {
	nums := []int{0, 1, 1}
	if n < 3 {
		return nums[n]
	} else {
		for i := 3; i <= n; i++ {
			nums = append(nums, nums[i-1]+nums[i-2]+nums[i-3])
		}
		return nums[len(nums)-1]
	}
}

// @lc code=end

