package main

// @leet start
func countGoodTriplets(arr []int, a int, b int, c int) int {
	// brute force
	abs := func(x int) int {
		if x < 0 {
			return -x
		}
		return x
	}
	n := len(arr)
	count := 0
	for i := 0; i < n-2; i++ {
		for j := i + 1; j < n-1; j++ {
			for k := j + 1; k < n; k++ {
				if abs(arr[i]-arr[j]) <= a && abs(arr[j]-arr[k]) <= b && abs(arr[i]-arr[k]) <= c {
					count++
				}
			}
		}
	}
	return count
}

// @leet end

