/*
 * @lc app=leetcode id=274 lang=golang
 *
 * [274] H-Index
 */

// @lc code=start
package main

import (
	"sort"
)

func hIndex(citations []int) int {
	// sort
	sort.Slice(citations, func(i, j int) bool {
		return citations[i] < citations[j]
	})
	// fmt.Println(citations)
	ans := 0
	for i := 0; i < len(citations); i++ {
		n := citations[i]
		nPapers := len(citations) - i
		// h is the min of two number
		var h int
		if n <= nPapers {
			h = n
		} else {
			h = nPapers
		}
		// update h
		if h > ans {
			ans = h
		}
	}
	return ans
}

// @lc code=end
