package main

// @leet start
func maximumTripletValue(nums []int) int64 {
	// maxVal[i] = the max val and idx pair in nums[i+1:]
	n := len(nums)
	maxVal := make([][]int, n)
	maxValPair := []int{nums[n-1], n - 1}
	for i := n - 2; i >= 0; i-- {
		num := nums[i]
		maxVal[i] = maxValPair
		if num >= maxValPair[0] {
			maxValPair = []int{num, i}
		}
	}
	ans := 0
	for i, num := range nums {
		if i >= n-2 {
			continue
		}
		for j := i + 1; j < n-1; j++ {
			if nums[j] >= num {
				continue
			}
			val := (num - nums[j]) * maxVal[j][0]
			if val > ans {
				ans = val
			}
		}
	}
	return int64(ans)
}

// @leet end

