/*
 * @lc app=leetcode id=2554 lang=golang
 *
 * [2554] Maximum Number of Integers to Choose From a Range I
 */

// @lc code=start
package main

type Set[T comparable] map[T]bool

func (s *Set[T]) Add(key T) {
	(*s)[key] = true
}

func (s *Set[T]) Has(key T) bool {
	_, ok := (*s)[key]
	return ok
}

func maxCount(banned []int, n int, maxSum int) int {
	bannedSet := Set[int]{}
	for _, n := range banned {
		bannedSet.Add(n)
	}

	c := 0
	s := 0
	i := 1
	for i <= n {
		if bannedSet.Has(i) {
			i++
			continue
		}
		if s+i <= maxSum {
			s += i
			i++
			c++
		} else {
			break
		}
	}
	return c
}

// @lc code=end
