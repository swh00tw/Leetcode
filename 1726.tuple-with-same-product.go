/*
 * @lc app=leetcode id=1726 lang=golang
 *
 * [1726] Tuple with Same Product
 */

// @lc code=start
package main

/*
1. brute force O(n^4)
2. two pointer O(n^3)
  - sort first
  - for each (l, r), find between them if any pair's product equal to nums[l]*nums[r], if found, count += 8
  - how to find? 2 pointers problem

3. O(n^2) https://leetcode.com/problems/tuple-with-same-product/solutions/6382282/efficient-python-solution-hashmap-counting-o-n-time-easiest-solution
*/
func tupleSameProduct(nums []int) int {
	ans := 0
	n := len(nums)
	prod := make(map[int]int)
	for i := 0; i < n; i++ {
		for j := 0; j < i; j++ {
			p := nums[i] * nums[j]
			ans += prod[p] * 8
			prod[p]++
		}
	}

	return ans
}

// @lc code=end
