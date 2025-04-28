package main

// @leet start
func countSubarrays(nums []int, k int64) int64 {
	// sol: https://leetcode.com/problems/count-subarrays-with-score-less-than-k/solutions/6666598/count-subarrays-with-score-less-than-k
	cnt := int64(0)
	l, r := 0, 0
	currSum := int64(0)
	for r < len(nums) {
		currSum += int64(nums[r])
		for l <= r && int64(r-l+1)*currSum >= k {
			currSum -= int64(nums[l])
			l++
		}
		cnt += int64(r - l + 1)
		r++
	}
	return cnt
}

// @leet end

