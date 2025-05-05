package main

// @leet start
func findMin(nums []int) int {
	// binary search
	// if nums[m-1] > nums[m] && nums[m+1] > nums[m] --> Find answer
	// if nums[r] < nums[m] --> Find answer in upper half
	// else, lower hald
	l, r := 0, len(nums)-1
	n := len(nums)
	for l <= r {
		m := (l + r) / 2
		lowerThanRightNum := false
		if m+1 < n {
			lowerThanRightNum = nums[m] < nums[m+1]
		} else {
			lowerThanRightNum = true
		}
		lowerThanLeftNum := false
		if m-1 >= 0 {
			lowerThanLeftNum = nums[m] < nums[m-1]
		} else {
			lowerThanLeftNum = true
		}
		if lowerThanRightNum && lowerThanLeftNum {
			return nums[m]
		}
		if nums[m] > nums[r] {
			l = m + 1
		} else {
			r = m - 1
		}
	}
	// should never reach here
	return nums[l]
}

// @leet end
