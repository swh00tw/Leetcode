package main

import "slices"

// @leet start
func findEvenNumbers(digits []int) []int {
	freq := make(map[int]int)
	for _, n := range digits {
		freq[n]++
	}
	var buildEvenNumbers func(freq map[int]int, remain int) []int
	buildEvenNumbers = func(freq map[int]int, remain int) []int {
		res := []int{}
		// base case, only look for even digit
		if remain == 1 {
			for k, v := range freq {
				if v > 0 && k%2 == 0 {
					res = append(res, k)
				}
			}
			slices.Sort(res)
			return res
		}
		// general case, need to avoid leading zero
		for k, v := range freq {
			if v == 0 {
				continue
			}
			if remain == 3 && k == 0 {
				continue
			}
			freq[k]--
			subans := buildEvenNumbers(freq, remain-1)
			if len(subans) > 0 {
				for _, n := range subans {
					if remain == 3 {
						res = append(res, k*100+n)
					} else if remain == 2 {
						res = append(res, k*10+n)
					}
				}
			}
			freq[k]++
		}
		return res
	}
	ans := buildEvenNumbers(freq, 3)
	slices.Sort(ans)
	return ans
}

// @leet end

