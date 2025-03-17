package main

import (
	"math"
	"slices"
)

// @leet start
func repairCars(ranks []int, cars int) int64 {
	// binary search between 1 and max(nums)*car^2 (worst case)
	// need a function to check if it's possible to fix in time
	l, r := 1, slices.Max(ranks)*cars*cars
	for l <= r {
		m := (l + r) / 2
		if isPossibleToFix(ranks, cars, m) {
			r = m - 1
		} else {
			l = m + 1
		}
	}
	return int64(l)
}

func isPossibleToFix(ranks []int, cars int, t int) bool {
	fixedCars := float64(0)
	for _, r := range ranks {
		// n = math.floor(sqrt(t/r))
		fixedCars += math.Floor(math.Sqrt(float64(t) / float64(r)))
	}
	return int(fixedCars) >= cars
}

// @leet end

