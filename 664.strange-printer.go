/*
 * @lc app=leetcode id=664 lang=golang
 *
 * [664] Strange Printer
 */

// @lc code=start
package main

import (
	"fmt"
)

var cache map[string]int

func toCacheKey(x, y int) string {
	return fmt.Sprintf("%d,%d", x, y)
}

func strangePrinter(s string) int {
	/*
	   1. preprocess: remove repeating chars
	   2. dp(start, end)
	   char x = s[start],
	   guess when did the printing at that round end,
	   let it end at idx k
	   the answer would be dp(start, k-1) + dp(k+1, end)
	   base case would be start > end, answer is 0
	*/
	cache = make(map[string]int)
	processedStr := ""
	for i := 0; i < len(s); i++ {
		c := s[i]
		if len(processedStr) == 0 {
			processedStr += string(c)
			continue
		}
		if processedStr[len(processedStr)-1] != c {
			processedStr += string(c)
		}
	}

	var getAns func(start, end int) int
	getAns = func(start, end int) int {
		// cache hit
		key := toCacheKey(start, end)
		if val, ok := cache[key]; ok {
			return val
		}
		// base case
		if start > end {
			return 0
		}
		firstChar := processedStr[start]
		// worst case, first char only repeat one time, no repeating char in rest string
		ans := 1 + getAns(start+1, end)
		for i := start + 1; i <= end; i++ {
			if processedStr[i] == firstChar {
				ans = min(ans, getAns(start, i-1)+getAns(i+1, end))
			}
		}
		// update cache
		cache[toCacheKey(start, end)] = ans
		return ans
	}

	return getAns(0, len(processedStr)-1)
}

// @lc code=end
