package main

// @leet start
func countSubarrays(nums []int) int {
	cnt := 0
	for i := 0; i < len(nums)-2; i++ {
		if 2*(nums[i]+nums[i+2]) == nums[i+1] {
			cnt++
		}
	}
	return cnt
}

// @leet end

