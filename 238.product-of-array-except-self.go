/*
 * @lc app=leetcode id=238 lang=golang
 *
 * [238] Product of Array Except Self
 */

// @lc code=start
func productExceptSelf(nums []int) []int {
	n := len(nums)

	prefixProduct := make([]int, n)
	acc := 1
	for i := 0; i < n; i++ {
		prefixProduct[i] = acc
		acc *= nums[i]
	}

	suffixProduct := make([]int, n)
	acc = 1
	for i := n - 1; i >= 0; i-- {
		suffixProduct[i] = acc
		acc *= nums[i]
	}

	ans := make([]int, n)
	for i := 0; i < n; i++ {
		ans[i] = suffixProduct[i] * prefixProduct[i]
	}
	return ans
}

// @lc code=end

