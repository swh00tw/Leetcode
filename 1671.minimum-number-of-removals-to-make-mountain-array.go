/*
 * @lc app=leetcode id=1671 lang=golang
 *
 * [1671] Minimum Number of Removals to Make Mountain Array
 */

// @lc code=start
package main

/*
ref: https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/solutions/5984835/python-dynamic-programming
*/
func minimumMountainRemovals(nums []int) int {
	n := len(nums)

	// Longest Increasing sequence for each idx i
	lis := make([]int, n)
	for i := 0; i < n; i++ {
		lis[i] = 1 // base ans
		for j := 0; j < i; j++ {
			if nums[j] < nums[i] {
				if lis[j]+1 > lis[i] {
					lis[i] = lis[j] + 1
				}
			}
		}
	}

	// Longest Decreasing sequence for each idx i
	lds := make([]int, n)
	for i := n - 1; i >= 0; i-- {
		lds[i] = 1 // base ans
		for j := i + 1; j < n; j++ {
			if nums[j] < nums[i] {
				if lds[j]+1 > lds[i] {
					lds[i] = lds[j] + 1
				}
			}
		}
	}

	maxMountainLen := 0
	for i, _ := range nums {
		if i == 0 || i == n-1 {
			continue
		}
		if lis[i] > 1 && lds[i] > 1 { // criteria for a valid peak
			l := lds[i] + lis[i] - 1
			if l >= maxMountainLen {
				maxMountainLen = l
			}
		}
	}

	return n - maxMountainLen
}

// @lc code=end
