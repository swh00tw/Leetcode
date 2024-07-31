/*
 * @lc app=leetcode id=62 lang=golang
 *
 * [62] Unique Paths
 */

// @lc code=start

import "math/big"

func product(n, lim int) *big.Int {
	res := big.NewInt(1)
	for ; n > lim; n-- {
		res = res.Mul(res, big.NewInt(int64(n)))
	}
	return res
}

func uniquePaths(m int, n int) int {
	// m columns, n rows
	if n == 1 || m == 1 {
		return 1
	}

	if n < m {
		m, n = n, m
	}
	ans := product(n+m-2, n-1).Div(product(n+m-2, n-1), product(m-1, 1))
	_ans, _ := bigIntToInt(ans)
	return _ans
}

// bigIntToInt safely converts a big.Int to an int, checking for overflow
func bigIntToInt(b *big.Int) (int, error) {
	if !b.IsInt64() {
		return 0, fmt.Errorf("value out of int64 range")
	}
	i64 := b.Int64()
	if i64 > math.MaxInt || i64 < math.MinInt {
		return 0, fmt.Errorf("value out of int range")
	}
	return int(i64), nil
}

// @lc code=end

