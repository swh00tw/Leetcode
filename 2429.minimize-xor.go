/*
 * @lc app=leetcode id=2429 lang=golang
 *
 * [2429] Minimize XOR
 */

// @lc code=start
package main

/*
  try to place all the 1s at the positions of 1s in num1, 2 cases
  1. if # of 1s in num2 <= # of 1s in num1, try to place 1s from higher bits
  2. if # of 1s in num2 > # of 1s in num1, try to place rest of 1s from lower bits
*/

func minimizeXor(num1 int, num2 int) int {
	bits1, ones1 := getBits(num1)
	_, ones2 := getBits(num2)
	// special case
	if ones1 == ones2 {
		return num1
	}
	if ones2 < ones1 {
		chances := ones1 - ones2
		idx := 0
		for chances > 0 {
			if bits1[idx] == 1 {
				bits1[idx] = 0
				chances--
			}
			idx++
		}
		return bitsToInt(bits1)
	}
	chances := ones2 - ones1
	idx := 0
	for chances > 0 {
		if idx >= len(bits1) {
			bits1 = append(bits1, 0)
		}
		if bits1[idx] == 0 {
			bits1[idx] = 1
			chances--
		}
		idx++
	}
	return bitsToInt(bits1)
}

func getBits(n int) ([]int, int) {
	numOf1s := 0
	ans := []int{}
	for n > 0 {
		b := n & 1
		ans = append(ans, b)
		if b == 1 {
			numOf1s++
		}
		n >>= 1
	}
	return ans, numOf1s
}

func bitsToInt(bits []int) int {
	curr := 0
	for i := 0; i < len(bits); i++ {
		curr += bits[i] * IntPow(2, i)
	}
	return curr
}

func IntPow(n, m int) int {
	if m == 0 {
		return 1
	}

	if m == 1 {
		return n
	}

	result := n
	for i := 2; i <= m; i++ {
		result *= n
	}
	return result
}

// @lc code=end
