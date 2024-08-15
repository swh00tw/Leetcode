/*
 * @lc app=leetcode id=452 lang=golang
 *
 * [452] Minimum Number of Arrows to Burst Balloons
 */

// @lc code=start
package main

import (
	"sort"
)

func findMinArrowShots(points [][]int) int {
	/*
			   schedule problem: greedy
			   1. get the minimum set of non-overlapped intervals
			   2. the answer if the length of the set since overlapped ballons can be removed when removing ballons in non-interval set
		    Note that the def of "overlap"
	*/
	n := len(points)
	sortedPoints := make([][]int, n)
	copy(sortedPoints, points)
	sort.Slice(sortedPoints, func(i, j int) bool {
		return sortedPoints[i][1] < sortedPoints[j][1]
	})

	numIntervals := 1
	prevIdx := 0
	for i := 1; i < n; i++ {
		if sortedPoints[i][0] > sortedPoints[prevIdx][1] {
			numIntervals++
			prevIdx = i
		}
	}
	return numIntervals
}

// @lc code=end
