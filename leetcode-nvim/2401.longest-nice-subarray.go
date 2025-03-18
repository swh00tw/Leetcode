package main

// @leet start
func longestNiceSubarray(nums []int) int {
	// sliding window
	n := len(nums)
	l := 0
	ans := 1
	for r := 1; r < n; r++ {
		num := nums[r]
		idx := r - 1
		for idx >= l {
			if num&nums[idx] == 0 {
				idx--
				continue
			}
			break
		}
		l = idx + 1
		if r-l+1 > ans {
			ans = r - l + 1
		}
	}
	return ans
}

// @leet end

