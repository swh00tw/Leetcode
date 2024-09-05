/*
 * @lc app=leetcode id=2028 lang=golang
 *
 * [2028] Find Missing Observations
 */

// @lc code=start
package main

func sum(nums []int) int {
	s := 0
	for _, num := range nums {
		s += num
	}
	return s
}

func missingRolls(rolls []int, mean int, n int) []int {
	m := len(rolls)
	diff := mean*(n+m) - sum(rolls)
	if diff < n || diff > 6*n {
		return []int{}
	}
	res := make([]int, n)
	quotient := diff / n
	mod := diff % n
	for i := 0; i < n; i++ {
		res[i] = quotient
		if mod > 0 {
			res[i]++
			mod--
		}
	}
	return res
}

// @lc code=end
