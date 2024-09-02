/*
 * @lc app=leetcode id=1894 lang=golang
 *
 * [1894] Find the Student that Will Replace the Chalk
 */

// @lc code=start
package main

func chalkReplacer(chalk []int, k int) int {
	// get the sum s of the chalks
	// get k = k mod s
	// linear traverse thru chalks and find where to stop
	s := 0
	for _, num := range chalk {
		s += num
	}
	chalks := k % s
	for i := 0; i < len(chalk); i++ {
		if chalks < chalk[i] {
			return i
		}
		chalks -= chalk[i]
	}
	// should never happen
	return -1
}

// @lc code=end
