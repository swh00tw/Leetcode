/*
 * @lc app=leetcode id=11 lang=golang
 *
 * [11] Container With Most Water
 */

// @lc code=start
package main

/*
volume = (right_idx - left_idx) * min(height[r], height[l])
two pointers, l, r := 0, n-1, where n = len(height)
ans := 0

	while l < r {
	  // keep updating ans if possible
	  ans = max(ans, formula)
	  // move whichever is lower between left or right
	}
*/
func maxArea(height []int) int {
	l, r := 0, len(height)-1
	ans := 0
	for l < r {
		volume := (r - l) * min(height[l], height[r])
		if volume > ans {
			ans = volume
		}
		if height[r] < height[l] {
			r--
		} else {
			l++
		}
	}
	return ans
}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

// @lc code=end
