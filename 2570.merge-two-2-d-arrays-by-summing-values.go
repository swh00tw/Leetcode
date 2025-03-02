/*
 * @lc app=leetcode id=2570 lang=golang
 *
 * [2570] Merge Two 2D Arrays by Summing Values
 */

// @lc code=start
package main

import "math"

func mergeArrays(nums1 [][]int, nums2 [][]int) [][]int {
	ans := [][]int{}
	n := len(nums1)
	m := len(nums2)
	i := 0
	j := 0
	for i < n || j < m {
		/*
		   if they point to the same id, merge and increment both pointers
		   else, append the id, val pair with smaller id
		*/
		id1 := math.MaxInt
		if i < n {
			id1 = nums1[i][0]
		}
		id2 := math.MaxInt
		if j < m {
			id2 = nums2[j][0]
		}
		if id1 == id2 {
			ans = append(ans, []int{id1, nums1[i][1] + nums2[j][1]})
			i++
			j++
			continue
		}
		if id1 < id2 {
			ans = append(ans, nums1[i])
			i++
		} else {
			ans = append(ans, nums2[j])
			j++
		}
	}
	return ans
}

// @lc code=end
