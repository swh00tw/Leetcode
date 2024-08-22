/*
 * @lc app=leetcode id=476 lang=golang
 *
 * [476] Number Complement
 */

// @lc code=start
package main

import "math"

func findComplement(num int) int {
	ans := 0
	pow := 0

	for num > 0 {
		// get last bit
		lastBit := num & 1
		// flip and add ans
		if lastBit == 0 {
			ans += int(math.Pow(2, float64(pow))) * 1
		}
		// increment pow
		pow++
		// update num (right shift one bit)
		num = num >> 1
	}
	return ans
}

// @lc code=end
