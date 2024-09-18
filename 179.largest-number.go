/*
 * @lc app=leetcode id=179 lang=golang
 *
 * [179] Largest Number
 */

// @lc code=start
package main

import (
	"sort"
	"strconv"
	"strings"
)

/*
  turn all int to string,
  sort by trying to concat two number and decide which one should come first
  ref: https://leetcode.com/problems/largest-number/solutions/5802534/python-greedy/?envType=daily-question&envId=2024-09-18
*/

func largestNumber(nums []int) string {
	n := len(nums)
	numStrings := make([]string, n)
	for i, num := range nums {
		numStrings[i] = strconv.Itoa(num)
	}
	sort.Slice(numStrings, func(i, j int) bool {
		if numStrings[i] == numStrings[j] {
			return true
		}
		res1 := numStrings[i] + numStrings[j]
		res2 := numStrings[j] + numStrings[i]
		return res1 > res2
	})
	ans := strings.Join(numStrings, "")
	if ans[0] == '0' {
		return "0"
	}
	return ans
}

// @lc code=end
