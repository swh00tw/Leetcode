/*
 * @lc app=leetcode id=2563 lang=golang
 *
 * [2563] Count the Number of Fair Pairs
 */

// @lc code=start
package main

import (
	"sort"
)

/*
use a var "count" to store ans
sort the nums

	for i, n := range nums {
	  use 2 binary search to find the leftmost idx and rightmost idx in array nums[i+1:]
	  so that we know how many pairs are fair which include idx i
	}
*/
func countFairPairs(nums []int, lower int, upper int) int64 {
	count := 0
	sort.Slice(nums, func(i, j int) bool {
		return nums[i] < nums[j]
	})

	for i, n := range nums {
		if i == len(nums)-1 {
			continue
		}
		rest := nums[i+1:]
		leftIdx := binarySearchLeft(rest, lower-n)
		if leftIdx == -1 {
			continue
		}
		rightIdx := binarySearchRight(rest, upper-n)
		if rightIdx == -1 {
			continue
		}
		count += rightIdx - leftIdx + 1
	}
	return int64(count)
}

func binarySearchLeft(arr []int, lower int) int {
	// find the leftmost item that larger than lower
	// if can't find, return -1
	if arr[len(arr)-1] < lower {
		return -1
	}
	l, r := 0, len(arr)-1
	for l <= r {
		m := (l + r) / 2
		if arr[m] >= lower {
			r = m - 1
		} else {
			l = m + 1
		}
	}
	return l
}

func binarySearchRight(arr []int, upper int) int {
	// find the rightmost item that lower than upper
	// if can't find, return -1
	if arr[0] > upper {
		return -1
	}
	l, r := 0, len(arr)-1
	for l <= r {
		m := (l + r) / 2
		if arr[m] > upper {
			r = m - 1
		} else {
			l = m + 1
		}
	}
	return l - 1
}

// @lc code=end
