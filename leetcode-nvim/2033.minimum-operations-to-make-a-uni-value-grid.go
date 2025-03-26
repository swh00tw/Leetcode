package main

import "slices"

// @leet start
// first, reduce to an array and sort it
// the difference of two number must be the multiple of x
// if not, return -1
// else, pick the middle number and calculate the steps needed
func minOperations(grid [][]int, x int) int {
	nums := []int{}
	for _, row := range grid {
		nums = append(nums, row...)
	}
	slices.Sort(nums)
	n := len(nums)
	for i := 0; i < n-1; i++ {
		if (nums[i+1]-nums[i])%x != 0 {
			return -1
		}
	}

	abs := func(x int) int {
		if x < 0 {
			return -x
		}
		return x
	}
	target := nums[(n-1)/2]
	steps := 0
	for _, num := range nums {
		steps += abs(target-num) / x
	}
	return steps
}

// @leet end
