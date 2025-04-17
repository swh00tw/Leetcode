package main

// @leet start
func countGood(nums []int, k int) int64 {
	// use a hashmap to store the freq
	// for each ending index, try shrinking the starting index
	// sliding window, the ans should be incremented by the value of starting idx
	ans := 0

	freq := make(map[int]int)
	pairs := 0
	start := 0
	for i, num := range nums {
		pairs += freq[num]
		freq[num]++
		// shrink start as much as possible, but make sure the the pairs are still at least k pairs
		for start < i {
			if pairs-(freq[nums[start]]-1) < k {
				break
			}
			freq[nums[start]]--
			pairs -= freq[nums[start]]
			start++
		}

		if pairs >= k {
			ans += start + 1
		}
	}
	return int64(ans)
}

// @leet end

