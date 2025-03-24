package main

import (
	"sort"
)

// @leet start
func countDays(days int, meetings [][]int) int {
	// sort the meeting by starrting time,
	// merge meetings if left.end >= right.start
	// ans = total days - meeting days
	sort.Slice(meetings, func(i, j int) bool {
		return meetings[i][0] < meetings[j][0]
	})
	intervals := [][]int{}
	curr := meetings[0]
	for i := 1; i < len(meetings); i++ {
		if curr[1] >= meetings[i][0] {
			// merge
			curr[1] = max(curr[1], meetings[i][1])
			continue
		}
		intervals = append(intervals, curr)
		curr = meetings[i]
	}
	intervals = append(intervals, curr)

	occupied := 0
	for _, interval := range intervals {
		occupied += interval[1] - interval[0] + 1
	}
	return days - occupied
}

// @leet end

