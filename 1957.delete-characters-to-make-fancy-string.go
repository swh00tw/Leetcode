/*
 * @lc app=leetcode id=1957 lang=golang
 *
 * [1957] Delete Characters to Make Fancy String
 */

// @lc code=start
package main

func makeFancyString(s string) string {
	ans := []byte{}
	for i, _ := range s {
		if i >= 2 {
			if s[i] == s[i-1] && s[i-1] == s[i-2] {
				continue
			}
		}
		ans = append(ans, s[i])
	}
	return string(ans)
}

// @lc code=end
