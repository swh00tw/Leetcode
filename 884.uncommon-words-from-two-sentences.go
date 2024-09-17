/*
 * @lc app=leetcode id=884 lang=golang
 *
 * [884] Uncommon Words from Two Sentences
 */

// @lc code=start
package main

import "strings"

func uncommonFromSentences(s1 string, s2 string) []string {
	set1 := make(map[string]int)
	set2 := make(map[string]int)
	words1 := strings.Split(s1, " ")
	words2 := strings.Split(s2, " ")

	for _, w := range words1 {
		if val, ok := set1[w]; ok {
			set1[w] = val + 1
		} else {
			set1[w] = 1
		}
	}
	for _, w := range words2 {
		if val, ok := set2[w]; ok {
			set2[w] = val + 1
		} else {
			set2[w] = 1
		}
	}

	ans := []string{}
	for _, w := range words1 {
		if _, ok := set2[w]; !ok {
			if set1[w] == 1 {
				ans = append(ans, w)
			}
		}
	}
	for _, w := range words2 {
		if _, ok := set1[w]; !ok {
			if set2[w] == 1 {
				ans = append(ans, w)
			}
		}
	}
	return ans
}

// @lc code=end
