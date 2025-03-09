package main

// @leet start
func numberOfAlternatingGroups(colors []int, k int) int {
	/*
	* ref: https://leetcode.com/problems/alternating-groups-ii/solutions/6447077/alternating-groups-ii
	 */
	for i := 0; i < k-1; i++ {
		colors = append(colors, colors[i])
	}
	n := len(colors)
	res := 0
	l, r := 0, 1
	for r < n {
		if colors[r] == colors[r-1] {
			l = r
			r++
			continue
		}
		r++
		if r-l < k {
			continue
		}
		res++
		l++
	}
	return res
}

// @leet end

