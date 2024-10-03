/*
 * @lc app=leetcode id=1590 lang=golang
 *
 * [1590] Make Sum Divisible by P
 */

// @lc code=start
package main

/*
  First, turn all nums => nums mod p
  Prepare prefixSum and suffixSum
  if sum is divisible, return 0
  for i=1 to i=n-1, find if the sum of the right side and left side of subarray is divisible by p
  return -1
*/

func minSubarray(nums []int, p int) int {
	n := len(nums)
	for i := 0; i < n; i++ {
		nums[i] = nums[i] % p
	}
	prefixSum := make([]int, n)
	curr := 0
	for i, n := range nums {
		prefixSum[i] = curr
		curr += n
	}
	suffixSum := make([]int, n)
	curr = 0
	for i := n - 1; i >= 0; i-- {
		suffixSum[i] = curr
		curr += nums[i]
	}
	// edge case
	if curr%p == 0 {
		return 0
	}
	for i := 1; i < n; i++ {
		for j := 0; j < n; j++ {
			right := prefixSum[j]
			if j+i-1 < n {
				left := suffixSum[j+i-1]
				s := left + right
				if s%p == 0 {
					return i
				}
			}
		}
	}
	return -1
}

// @lc code=end
