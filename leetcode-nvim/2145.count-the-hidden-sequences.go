package main

// @leet start
func numberOfArrays(differences []int, lower int, upper int) int {
	// parse the differences then know the loweset delta and highest delta
	// then the numbers between lower+lowest delta and upper-highest delta are valid
	lowest, highest := 0, 0
	curr := 0
	for _, num := range differences {
		curr += num
		if curr < lowest {
			lowest = curr
		}
		if curr > highest {
			highest = curr
		}
	}
	lowesetPossibleStart := lower - lowest
	highestPossibleStart := upper - highest
	ans := highestPossibleStart - lowesetPossibleStart + 1
	if ans < 0 {
		return 0
	}
	return ans
}

// @leet end

