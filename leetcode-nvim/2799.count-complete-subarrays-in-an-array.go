package main

// @leet start
func countCompleteSubarrays(nums []int) int {
	// ans is an array of length n, ans[i] is the number of complete subarrays start at i
	// first get the number of distinct elements in nums
	numDistinct := 0
	seen := make(map[int]bool)
	for _, num := range nums {
		seen[num] = true
	}
	numDistinct = len(seen)
	// filling ans array use a sliding window
	n := len(nums)
	ans := make([]int, n)
	freq := make(map[int]int) // the freq in window
	r := 0
	idx := 0
	for idx < n {
		// if the window is not complete, move r
		for len(freq) < numDistinct && r < n {
			freq[nums[r]]++
			r++
		}
		// record ans[idx]
		if len(freq) == numDistinct {
			ans[idx] = n + 1 - r
		}
		// move idx by 1
		freq[nums[idx]]--
		if freq[nums[idx]] == 0 {
			delete(freq, nums[idx])
		}
		idx++
	}
	sum := 0
	for _, v := range ans {
		sum += v
	}
	return sum
}

// @leet end

