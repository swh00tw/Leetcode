package main

// @leet start
func maximumCount(nums []int) int {
	neg := binarySearchLeft(nums, 0)
	pos := len(nums) - binarySearchRight(nums, 0)
	if neg > pos {
		return neg
	}
	return pos
}

func binarySearchLeft(nums []int, target int) int {
	n := len(nums)
	l, r := 0, n-1
	for l <= r {
		m := (l + r) / 2
		if nums[m] == target {
			r = m - 1
			continue
		}
		if nums[m] < target {
			l = m + 1
		} else {
			r = m - 1
		}
	}
	return l
}

func binarySearchRight(nums []int, target int) int {
	n := len(nums)
	l, r := 0, n-1
	for l <= r {
		m := (l + r) / 2
		if nums[m] == target {
			l = m + 1
			continue
		}
		if nums[m] < target {
			l = m + 1
		} else {
			r = m - 1
		}
	}
	return l
}

// @leet end

