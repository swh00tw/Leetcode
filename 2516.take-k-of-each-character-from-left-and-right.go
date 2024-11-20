/*
 * @lc app=leetcode id=2516 lang=golang
 *
 * [2516] Take K of Each Character From Left and Right
 */

// @lc code=start
package main

func takeCharacters(s string, k int) int {
	/*
	   use sliding window to find the MAXIMUM subarray that we can remove so that the rest of parts satisfy the requirement
	   keep growing the window by incrementing right pointer UNTIL we take too many characters that will result in no answer
	   if we take too many, keep shrinking the window by incrementing left pointer
	*/

	// edge case
	freq := make(map[rune]int)
	for _, c := range s {
		freq[c]++
	}

	maximumAllowed := make(map[rune]int)
	for _, c := range []rune{'a', 'b', 'c'} {
		if freq[c] < k {
			return -1
		}
		maximumAllowed[c] = freq[c] - k
	}

	l := 0
	r := 0
	window := make(map[rune]int)
	ans := len(s)
	for r < len(s) {
		window[rune(s[r])]++
		if window['a'] > maximumAllowed['a'] || window['b'] > maximumAllowed['b'] || window['c'] > maximumAllowed['c'] {
			window[rune(s[l])]--
			l++
		}
		ans = min(ans, len(s)-(r-l+1))
		r++
	}

	return ans
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

// @lc code=end
