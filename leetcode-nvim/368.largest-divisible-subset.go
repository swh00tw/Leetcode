package main

import (
	"slices"
)

// @leet start
func largestDivisibleSubset(nums []int) []int {
	// sort first
	// for every number, get subset
	n := len(nums)
	slices.Sort(nums)

	cache := make(map[int][]int)
	// get the largest subset include current number
	var getLargestSubset func(start int) []int
	getLargestSubset = func(start int) []int {
		if v, ok := cache[start]; ok {
			return v
		}
		// base base
		if start == n-1 {
			return []int{nums[start]}
		}
		if start >= n {
			return []int{}
		}
		res := []int{nums[start]}
		current := nums[start]
		for i := start + 1; i < n; i++ {
			if nums[i]%current != 0 {
				continue
			}
			subans := []int{current}
			subans = append(subans, getLargestSubset(i)...)
			if len(subans) > len(res) {
				res = subans
			}
		}
		cache[start] = res
		return res
	}

	ans := []int{}
	for i := range nums {
		subans := getLargestSubset(i)
		if len(subans) > len(ans) {
			ans = subans
		}
	}
	return ans
}

// @leet end

