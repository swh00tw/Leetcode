package main

// @leet start
func findMissingAndRepeatedValues(grid [][]int) []int {
	// create a set contains 1 to n^2
	// when encounter a number, remove it from the set
	// if remove a number which is already removed, it is the repeated number
	// the last number in the set is the missing number
	numbers := map[int]bool{}
	n := len(grid)
	for i := 1; i <= n*n; i++ {
		numbers[i] = true
	}
	ans := []int{0, 0}
	for _, row := range grid {
		for _, cell := range row {
			if _, ok := numbers[cell]; ok {
				delete(numbers, cell)
			} else {
				ans[0] = cell
			}
		}
	}
	for key := range numbers {
		ans[1] = key
	}
	return ans
}

// @leet end

