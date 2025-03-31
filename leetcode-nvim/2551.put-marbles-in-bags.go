package main

import (
	"slices"
)

// @leet start
func putMarbles(weights []int, k int) int64 {
	// k bags --> (k-1) cuts
	// find the value of all cuts, sort
	// the smallest distribution is the smallest k-1 cuts
	// the largest distribution is the largest k-1 cuts
	cuts := []int{}
	for i, v := range weights {
		if i == 0 {
			continue
		}
		cuts = append(cuts, v+weights[i-1])
	}
	slices.Sort(cuts)
	n := len(cuts)
	ans := 0
	for i := 0; i < k-1; i++ {
		ans += cuts[n-1-i] - cuts[i]
	}
	return int64(ans)
}

// @leet end

