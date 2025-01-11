/*
 * @lc app=leetcode id=1400 lang=golang
 *
 * [1400] Construct K Palindrome Strings
 */

// @lc code=start
package main

func canConstruct(s string, k int) bool {
	// edge case
	if k > len(s) {
		return false
	}
	if k == len(s) {
		return true
	}
	// get char freq, if the number of "odd" char exceed k, return false
	// else, return true
	charFreq := make(map[rune]int)
	for _, c := range s {
		charFreq[c]++
	}
	odd := 0
	for _, v := range charFreq {
		if v%2 == 1 {
			odd++
		}
	}
	if odd > k {
		return false
	}
	return true
}

// @lc code=end
