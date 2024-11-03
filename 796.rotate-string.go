/*
 * @lc app=leetcode id=796 lang=golang
 *
 * [796] Rotate String
 */

// @lc code=start
package main

import "strings"

func rotateString(s string, goal string) bool {
	s2 := s + s
	return len(s) == len(goal) && strings.Contains(s2, goal)
}

// @lc code=end
