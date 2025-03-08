package main

// @leet start
// slding window
// the window size is k
// keep track of how many recolors
func minimumRecolors(blocks string, k int) int {
	n := len(blocks)
	recolor := 0
	for i := 0; i < k; i++ {
		if blocks[i] != 'B' {
			recolor++
		}
	}
	ans := recolor
	for right := k; right < n; right++ {
		if blocks[right] != 'B' {
			recolor++
		}
		if blocks[right-k] != 'B' {
			recolor--
		}
		if recolor < ans {
			ans = recolor
		}
	}
	return ans
}

// @leet end

