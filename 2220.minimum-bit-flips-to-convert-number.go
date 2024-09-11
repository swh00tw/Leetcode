/*
 * @lc app=leetcode id=2220 lang=golang
 *
 * [2220] Minimum Bit Flips to Convert Number
 */

// @lc code=start
package main

func getLastBit(n int) int {
	lastBit := n & 1
	return lastBit
}

func minBitFlips(start int, goal int) int {
	count := 0
	for start > 0 || goal > 0 {
		b1 := getLastBit(start)
		b2 := getLastBit(goal)
		// fmt.Println(b1, b2)
		if b1 != b2 {
			count++
		}
		start >>= 1
		goal >>= 1
	}
	return count
}

// @lc code=end
