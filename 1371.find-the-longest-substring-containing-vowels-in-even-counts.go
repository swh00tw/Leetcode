/*
 * @lc app=leetcode id=1371 lang=golang
 *
 * [1371] Find the Longest Substring Containing Vowels in Even Counts
 */

// @lc code=start
package main

// ref:https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/solutions/5788167/easiest-approach-fully-explained-must-watch

func findTheLongestSubstring(s string) int {
	mask := 0
	maskmap := make(map[int]int) // map from first occurence of mask to idx
	maskmap[0] = -1              // handle case that substring start from 0
	best := 0
	for i, l := range s {
		switch l {
		case 'a':
			mask ^= (1 << 0)
		case 'e':
			mask ^= (1 << 1)
		case 'i':
			mask ^= (1 << 2)
		case 'o':
			mask ^= (1 << 3)
		case 'u':
			mask ^= (1 << 4)
		}

		if val, ok := maskmap[mask]; ok {
			if i-val > best {
				best = i - val
			}
		} else {
			maskmap[mask] = i
		}
	}
	return best
}

// @lc code=end
