/*
 * @lc app=leetcode id=1574 lang=golang
 *
 * [1574] Shortest Subarray to be Removed to Make Array Sorted
 */

// @lc code=start
package main

/*
subarray is a contiguous subseq
1. find the longest non-decreasing subarr from front
2. find the longest non-decreasing subarr from right
3. remove the item in the middle, and try to merge two subarr by deleting some items
*/
func findLengthOfShortestSubarray(arr []int) int {
	left := 0
	for left < len(arr)-1 && arr[left] <= arr[left+1] {
		left++
	}

	// early stop
	// if already sorted
	if left == len(arr)-1 {
		return 0
	}

	right := len(arr) - 1
	for right > 0 && arr[right] >= arr[right-1] {
		right--
	}

	minDelete := min(len(arr)-left-1, right)
	i, j := 0, right
	for i <= left && j < len(arr) {
		if arr[i] <= arr[j] {
			// update ans
			delete := j - i - 1
			minDelete = min(minDelete, delete)
			i++
		} else {
			j++
		}
	}
	return minDelete
}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

// @lc code=end
