/*
 * @lc app=leetcode id=242 lang=golang
 *
 * [242] Valid Anagram
 */

// @lc code=start
package main

/*
1. use a hashmap, map from rune to freq of string s
2. parse string t, and decrement the value of rune if we meet one
3. if the value of hashmap is zero, remove key
*/
func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}
	freq := make(map[rune]int)
	for _, c := range s {
		freq[c]++
	}
	for _, c := range t {
		if val, ok := freq[c]; ok {
			freq[c]--
			if val == 1 {
				delete(freq, c)
			}
			continue
		}
		return false
	}
	return true
}

// @lc code=end
