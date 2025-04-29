package main

// @leet start
func countSubarrays(nums []int, k int) int64 {
	// maintain a sliding window
	// extend when the number of max element is less than k
	// shrink when the number of max element is greater than k
	// ans[i] is the valid subarray count that ends at i
	// ans[i] is the value of left pointer+1
	n := len(nums)
	maxNum := nums[0]
	for i := 1; i < n; i++ {
		if nums[i] > maxNum {
			maxNum = nums[i]
		}
	}
	ans := make([]int64, n)
	l, r := 0, 0
	numMax := 0
	for r = 0; r < n; r++ {
		if nums[r] == maxNum {
			numMax++
		}
		for numMax > k {
			if nums[l] == maxNum {
				numMax--
			}
			l++
		}
		// if nums[l] is not maxNum, we need to move l to the next maxNum
		for l < n && nums[l] != maxNum {
			l++
		}

		if numMax == k {
			ans[r] = int64(l + 1)
		}
	}
	sum := int64(0)
	for _, a := range ans {
		sum += a
	}
	return sum
}

// @leet end

