/*
 * @lc app=leetcode id=58 lang=golang
 *
 * [58] Length of Last Word
 */

// @lc code=start
package main

import "strings"

func lengthOfLastWord(s string) int {
	ans := 0
	words := strings.Split(s, " ")
	for _, w := range words {
		if len(w) == 0 {
			continue
		}
		ans = len(w)
	}
	return ans
}

// @lc code=end
