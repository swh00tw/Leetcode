/*
 * @lc app=leetcode id=2425 lang=golang
 *
 * [2425] Bitwise XOR of All Pairings
 */

// @lc code=start
package main

/*
  n = len(nums1), m = len(nums2)
  there are m nums1[0], nums1[1], ...
  there are n nums2[0], nums2[1], ...
  if n, m is even num, result in 0, else remain itself
  XOR all remaining together
*/

func xorAllNums(nums1 []int, nums2 []int) int {
	n := len(nums1)
	m := len(nums2)
	xor1 := 0
	if m%2 == 1 {
		for _, num := range nums1 {
			xor1 ^= num
		}
	}
	xor2 := 0
	if n%2 == 1 {
		for _, num := range nums2 {
			xor2 ^= num
		}
	}
	return xor1 ^ xor2
}

// @lc code=end
