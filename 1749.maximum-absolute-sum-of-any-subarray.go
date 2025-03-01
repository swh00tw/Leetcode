/*
 * @lc app=leetcode id=1749 lang=golang
 *
 * [1749] Maximum Absolute Sum of Any Subarray
 */

// @lc code=start

package main

/*
1. prefix sum, 2 pointer
2. negate all integers and do it again
*/
func maxAbsoluteSum(nums []int) int {
	ans1 := getMaxSubarrayVal(getPrefixSum(nums))
	neg := []int{}
	for _, n := range nums {
		neg = append(neg, -n)
	}
	ans2 := getMaxSubarrayVal(getPrefixSum(neg))
	if ans1 > ans2 {
		return ans1
	}
	return ans2
}

func getPrefixSum(num []int) []int {
	prefixSum := []int{0}
	curr := 0
	for _, n := range num {
		curr += n
		prefixSum = append(prefixSum, curr)
	}
	return prefixSum
}
func getMaxSubarrayVal(num []int) int {
	ans := 0
	l := 0
	n := len(num)
	for r := 0; r < n; r++ {
		if num[r] > num[l] {
			if num[r]-num[l] > ans {
				ans = num[r] - num[l]
			}
		} else {
			l = r
		}
	}
	return ans
}

// @lc code=end
