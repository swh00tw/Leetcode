/*
 * @lc app=leetcode id=1318 lang=golang
 *
 * [1318] Minimum Flips to Make a OR b Equal to c
 */

// @lc code=start
package main

/*
keet get rightmost bit
and count how many bit need to flip bit-by-bit from right to left
*/

func minFlips(a int, b int, c int) int {
	var flipsCount = 0

	for a > 0 || b > 0 || c > 0 {
		var bitC = c & 1
		var bitA = a & 1
		var bitB = b & 1

		if bitC == 1 {
			if bitA == 0 && bitB == 0 {
				flipsCount++
			}
		} else {
			if bitA == 1 {
				flipsCount++
			}

			if bitB == 1 {
				flipsCount++
			}
		}

		c >>= 1
		a >>= 1
		b >>= 1
	}

	return flipsCount
}

// @lc code=end
