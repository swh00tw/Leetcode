/*
 * @lc app=leetcode id=42 lang=golang
 *
 * [42] Trapping Rain Water
 */

// @lc code=start
package main

import "slices"

/*
use a 2d array to represent the graph, m*3
n = len(hright)
m = max_height
For each height, store 3 nums
1. lowest point
2. highest point
3. number of cell at this height

iterate from 0 to max_height,
count how many empty missing number in array from lowest to height
heighest - (lowest -1) - num_of_cells
*/
func trap(height []int) int {
	m := slices.Max(height)
	graph := make([][]int, m)
	for i := 0; i < m; i++ {
		graph[i] = []int{-1, -1, 0}
	}

	for i, h := range height {
		for j := 0; j < h; j++ {
			if graph[j][0] == -1 {
				graph[j][0] = i
			} else {
				graph[j][1] = i
			}
			graph[j][2]++
		}
	}

	count := 0
	for i := 0; i < m; i++ {
		level := graph[i]
		if level[2] > 1 {
			count += level[1] - level[0] + 1 - level[2]
		}
	}
	return count
}

// @lc code=end
