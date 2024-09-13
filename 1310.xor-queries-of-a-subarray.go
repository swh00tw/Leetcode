/*
 * @lc app=leetcode id=1310 lang=golang
 *
 * [1310] XOR Queries of a Subarray
 */

// @lc code=start
package main

func xorQueries(arr []int, queries [][]int) []int {
	/*
	   prefixXOR
	   build an arr prefixXOR such that arr[i] = arr[0]^arr[1]...^arr[i]
	   xor from idx i to j is prefixXOR[j]^prefixXOR[i-1] if i != 0, else prefixXOR[j]
	*/
	n := len(arr)
	prefixXOR := make([]int, n)
	xor := 0
	for i := 0; i < n; i++ {
		xor ^= arr[i]
		prefixXOR[i] = xor
	}
	ans := make([]int, len(queries))
	for i, q := range queries {
		start, end := q[0], q[1]
		if start == 0 {
			ans[i] = prefixXOR[end]
		} else {
			ans[i] = prefixXOR[end] ^ prefixXOR[start-1]
		}
	}
	return ans
}

// @lc code=end
