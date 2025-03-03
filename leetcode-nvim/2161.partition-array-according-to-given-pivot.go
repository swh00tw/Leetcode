package main

// @leet start
func pivotArray(nums []int, pivot int) []int {
	less := []int{}
	equal := []int{}
	greater := []int{}
	for _, n := range nums {
		if n == pivot {
			equal = append(equal, n)
		} else if n < pivot {
			less = append(less, n)
		} else {
			greater = append(greater, n)
		}
	}
	ans := []int{}
	ans = append(ans, less...)
	ans = append(ans, equal...)
	ans = append(ans, greater...)
	return ans
}

// @leet end

