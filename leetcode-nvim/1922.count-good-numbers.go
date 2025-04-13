package main

// @leet start
// ref: https://leetcode.com/problems/count-good-numbers/solutions/6581822/count-good-numbers
func countGoodNumbers(n int64) int {
	mod := int64(1e9 + 7)
	// use fast exponentiation to calculate x^y % mod
	quickmul := func(x, y int64) int64 {
		ret := int64(1)
		mul := x
		for y > 0 {
			if y%2 == 1 {
				ret = ret * mul % mod
			}
			mul = mul * mul % mod
			y /= 2
		}
		return ret
	}

	oddIndices := n / 2
	evenIndices := n - oddIndices
	return int(quickmul(5, evenIndices) * quickmul(4, oddIndices) % mod)
}

// @leet end

