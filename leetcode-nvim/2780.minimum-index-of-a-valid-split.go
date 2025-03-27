package main

// @leet start
func minimumIndex(nums []int) int {
	// create an array scuh that arr[i] = dominant number in nums[i+1:]
	// create an array such that arr[i] = dominant number in nums[:i+1]
	n := len(nums)
	right := make([]int, n)
	left := make([]int, n)
	for i := 0; i < n; i++ {
		right[i] = -1
		left[i] = -1
	}
	freq := make(map[int]int)
	dominant := -1
	for i := 0; i < n; i++ {
		key := nums[i]
		freq[key]++
		if freq[key]*2 > (i + 1) {
			dominant = key
		}
		// reset dominant to -1 if no dominant
		if freq[dominant]*2 <= (i + 1) {
			dominant = -1
		}
		left[i] = dominant
	}
	freq = make(map[int]int)
	dominant = -1
	for i := n - 1; i >= 0; i-- {
		key := nums[i]
		right[i] = dominant
		freq[key]++
		if freq[key]*2 > (n - i) {
			dominant = key
		}
		// reset dominant to -1 if no dominant
		if freq[dominant]*2 <= (n - i) {
			dominant = -1
		}
	}
	ans := -1
	for i := 0; i < n-1; i++ {
		if left[i] == right[i] {
			ans = i
			break
		}
	}
	return ans
}

// @leet end

