/*
 * @lc app=leetcode id=214 lang=golang
 *
 * [214] Shortest Palindrome
 */

// @lc code=start
package main

/*
Find longest palindrome from index 0
*/
func shortestPalindrome(s string) string {
	n := len(s)
	if n <= 1 {
		return s
	}
	longestPalindrome := 1
	for i := 1; i < n; i++ {
		if s[i] != s[0] {
			continue
		}
		if isPalindrome(s, 0, i) {
			longestPalindrome = i + 1
		}
	}
	suffix := s[longestPalindrome:]
	return reverseString(suffix) + s
}

func isPalindrome(s string, i, j int) bool {
	/*
	   Check if s[i:j+1] is palindrome
	*/
	for i < j {
		if s[i] != s[j] {
			return false
		}
		i++
		j--
	}

	return true
}

func reverseString(s string) string {
	/*
	   Reverse a string
	*/
	n := len(s)
	runes := []rune(s)
	for i := 0; i < n/2; i++ {
		runes[i], runes[n-i-1] = runes[n-i-1], runes[i]
	}
	return string(runes)
}

// @lc code=end
