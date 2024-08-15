/*
 * @lc app=leetcode id=435 lang=golang
 *
 * [435] Non-overlapping Intervals
 */

// @lc code=start
package main

import (
	"sort"
)

func eraseOverlapIntervals(intervals [][]int) int {
	/*
	   schedule problem: greedy
	   1. sort the intervals by end time
	   2. pick first
	   3. keep picking, skip if overlap
	*/
	sortedIntervals := make([][]int, len(intervals))
	copy(sortedIntervals, intervals)
	sort.Slice(sortedIntervals, func(i, j int) bool {
		if sortedIntervals[i][1] == sortedIntervals[j][1] {
			return sortedIntervals[i][0] < sortedIntervals[j][0]
		}
		return sortedIntervals[i][1] < sortedIntervals[j][1]
	})

	n := len(intervals)
	numIntervals := 1
	prevIdx := 0
	for i := 1; i < n; i++ {
		if sortedIntervals[i][0] >= sortedIntervals[prevIdx][1] {
			numIntervals++
			prevIdx = i
		}
	}

	return n - numIntervals
}

// @lc code=end
