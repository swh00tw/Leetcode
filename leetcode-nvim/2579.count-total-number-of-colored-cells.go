package main

// @leet start
func coloredCells(n int) int64 {
	/*
			    1. every minute, the number of cells grow is d_i
		      2. d_i = 4 + d_{i-1}
			* */
	deltas := []int{0}
	init := int64(1)
	for len(deltas) < n {
		prev := deltas[len(deltas)-1]
		deltas = append(deltas, 4+prev)
		init += int64(4 + prev)
	}
	return init
}

// @leet end

