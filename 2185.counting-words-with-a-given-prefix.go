/*
 * @lc app=leetcode id=2185 lang=golang
 *
 * [2185] Counting Words With a Given Prefix
 */

// @lc code=start
package main

import "strings"

func prefixCount(words []string, pref string) int {
	cnt := 0
	for _, w := range words {
		if strings.HasPrefix(w, pref) {
			cnt++
		}
	}
	return cnt
}

// @lc code=end
