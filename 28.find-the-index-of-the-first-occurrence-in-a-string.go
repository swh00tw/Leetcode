/*
 * @lc app=leetcode id=28 lang=golang
 *
 * [28] Find the Index of the First Occurrence in a String
 */

// @lc code=start
package main

/*
n = len(needle)
m = len(haystack)
for i = 0;i < m-1;i++

	substr = haystack[i:i+n] // if out of range, ignore
	if substr == needle:
	  return i

return -1
*/
func strStr(haystack string, needle string) int {
	n := len(needle)
	m := len(haystack)
	for i, _ := range haystack {
		if i+n > m {
			continue
		}
		substr := haystack[i : i+n]
		if substr == needle {
			return i
		}
	}
	return -1
}

// @lc code=end
