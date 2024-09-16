/*
 * @lc app=leetcode id=539 lang=golang
 *
 * [539] Minimum Time Difference
 */

// @lc code=start
package main

import (
	"math"
	"sort"
	"strconv"
	"strings"
)

func findMinDifference(timePoints []string) int {
	/*
	   sort the arr,
	   append the first item to the last,
	   find the min diff
	*/
	n := len(timePoints)
	ts := make([]int, len(timePoints))
	for i, tp := range timePoints {
		hrMin := strings.Split(tp, ":")
		hr, min := hrMin[0], hrMin[1]
		h, _ := strconv.Atoi(hr)
		m, _ := strconv.Atoi(min)
		ts[i] = h*60 + m
	}
	// sort
	sort.Slice(ts, func(i, j int) bool {
		return ts[i] < ts[j]
	})

	ts = append(ts, ts[0])
	diff := math.MaxInt
	day := 24 * 60
	for i := 0; i < n; i++ {
		d := (ts[i+1] - ts[i] + day) % day
		if d < diff {
			diff = d
		}
	}
	return diff
}

// @lc code=end
