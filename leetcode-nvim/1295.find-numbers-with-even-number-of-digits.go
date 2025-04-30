package main

// @leet start
func findNumbers(nums []int) int {
	// since the number is within 10^5, just brute force
	cnt := 0
	for _, n := range nums {
		if n >= 10 && n < 100 {
			cnt++
			continue
		}
		if n >= 1000 && n < 10000 {
			cnt++
			continue
		}
		if n >= 100000 && n < 10000000 {
			cnt++
			continue
		}
	}
	return cnt
}

// @leet end

