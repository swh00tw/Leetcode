package main

import "sort"

// @leet start
func countFairPairs(nums []int, lower int, upper int) int64 {
	insertSorted := func(arr []int, num int) []int {
		idx := sort.Search(len(arr), func(i int) bool { return arr[i] >= num })
		arr = append(arr, 0) // make space for the new element
		copy(arr[idx+1:], arr[idx:])
		arr[idx] = num
		return arr
	}
	binarySearchRight := func(arr []int, target int) int {
		// find rightmost index of target
		l, r := 0, len(arr)-1
		for l <= r {
			m := (l + r) / 2
			if arr[m] <= target {
				l = m + 1
			} else {
				r = m - 1
			}
		}
		return l
	}
	count := 0
	processed := []int{} // sorted array of processed numbers
	for _, num := range nums {
		// use binary search to find the range of valid pairs
		rightIdx := binarySearchRight(processed, upper-num)
		leftIdx := binarySearchRight(processed, lower-num-1)
		count += rightIdx - leftIdx
		// insert into processed in sorted order
		processed = insertSorted(processed, num)
	}
	return int64(count)
}

// @leet end

