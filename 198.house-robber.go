/*
 * @lc app=leetcode id=198 lang=golang
 *
 * [198] House Robber
 */

// @lc code=start
func rob(nums []int) int {
	// each house i, the best answer is either rob or not rob
	// (the value of this house + answer from i-2) or (answer from i-1)
	n := len(nums)
	ans := make([]int, n)
	for i, val := range nums {
		if i == 0 {
			ans[i] = val
			continue
		}
		prevAns := 0
		if i-2 >= 0 {
			prevAns = ans[i-2]
		}
		ans[i] = max(prevAns+val, ans[i-1])
	}
	return ans[n-1]
}

// @lc code=end

