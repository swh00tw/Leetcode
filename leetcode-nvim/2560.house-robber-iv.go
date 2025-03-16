package main

import "slices"

// @leet start
func minCapability(nums []int, k int) int {
	l, r := slices.Min(nums), slices.Max(nums)
	for l <= r {
		m := (l + r) / 2
		if checkCapabilityPossible(nums, k, m) {
			r = m - 1
		} else {
			l = m + 1
		}
	}
	return l
}

func checkCapabilityPossible(nums []int, k int, c int) bool {
	cnt := 0
	n := len(nums)
	i := 0
	for i < n {
		if nums[i] <= c {
			cnt++
			i += 2
			continue
		}
		i++
	}
	return cnt >= k
}

// @leet end
