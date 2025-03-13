package main

// @leet start
func minZeroArray(nums []int, queries [][]int) int {
	// binary search and use canFormZeroArray to check if the query is valid
	n := len(queries)
	if !canFormZeroArray(nums, queries) {
		return -1
	}
	l, r := 0, n-1
	for l <= r {
		m := (l + r) / 2
		if canFormZeroArray(nums, queries[:m]) {
			r = m - 1
		} else {
			l = m + 1
		}
	}
	return l
}

func canFormZeroArray(nums []int, queries [][]int) bool {
	// use differential array to store processed queries
	// the prefix sum of the diff array is the result of the query
	// goal: make prefixSumOfDiffArray[i] >= nums[i] for all i
	n := len(nums)
	diff := make([]int, n+1)
	for _, q := range queries {
		l, r, val := q[0], q[1], q[2]
		diff[l] += val
		diff[r+1] -= val
	}
	// reconstruct the array
	prefixSum := 0
	for i := 0; i < n; i++ {
		prefixSum += diff[i]
		if prefixSum < nums[i] {
			return false
		}
	}
	return true
}

// @leet end

