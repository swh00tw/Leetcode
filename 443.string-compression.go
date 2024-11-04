/*
 * @lc app=leetcode id=443 lang=golang
 *
 * [443] String Compression
 */

// @lc code=start
package main

import (
	"strconv"
)

func compress(chars []byte) int {
	read_idx := 0
	write_idx := 0
	n := len(chars)
	for read_idx < n {
		char := chars[read_idx]
		// get how many char
		times := 0
		for read_idx < n && chars[read_idx] == char {
			read_idx++
			times++
		}
		chars[write_idx] = char
		write_idx++
		if times > 1 {
			times_str := strconv.Itoa(times)
			for j := 0; j < len(times_str); j++ {
				chars[write_idx] = times_str[j]
				write_idx++
			}
		}
	}
	return write_idx
}

// @lc code=end
