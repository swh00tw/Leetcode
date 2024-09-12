/*
 * @lc app=leetcode id=1684 lang=golang
 *
 * [1684] Count the Number of Consistent Strings
 */

// @lc code=start
package main

func countConsistentStrings(allowed string, words []string) int {
	allowedRune := make(map[rune]bool)
	for _, r := range allowed {
		allowedRune[r] = true
	}
	count := 0
	for _, w := range words {
		isConsistent := true
		for _, r := range w {
			if _, ok := allowedRune[r]; !ok {
				isConsistent = false
			}
		}
		if isConsistent {
			count++
		}
	}
	return count
}

// @lc code=end
