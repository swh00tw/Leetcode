package main

import "slices"

// @leet start
func maximumCandies(candies []int, k int64) int {
	// use binary search, answer is 0 to max(candies)
	// write a function (candies, target) to check if it is possible to allocate candies
	// first, check if target*k <= total candies, if no, return false
	// then, candies.map((v) => v/target).reduce((cur, acc) -> acc+=cur,0) --> total valid piles
	// if total valid piles >= k, return true, else false
	l, r := 1, slices.Max(candies)
	totalCandies := int64(0)
	for _, v := range candies {
		totalCandies += int64(v)
	}
	for l <= r {
		m := (l + r) / 2
		if canAllocated(candies, k, int64(m), totalCandies) {
			l = m + 1
		} else {
			r = m - 1
		}
	}
	return r
}

func canAllocated(candies []int, k int64, target int64, totalCandies int64) bool {
	if target*k > totalCandies {
		return false
	}
	piles := make([]int64, len(candies))
	for i, c := range candies {
		piles[i] = int64(c) / target
	}
	validPiles := int64(0)
	for _, p := range piles {
		validPiles += p
	}
	return int64(validPiles) >= k
}

// @leet end

