package main

// @leet start
func checkPowersOfThree(n int) bool {
	_, noRepeat := getPowersOfThree(n)
	return noRepeat
}

func getPowersOfThree(n int) ([]int, bool) {
	powers := []int{}
	if n < 0 {
		return powers, false
	}
	if n == 0 {
		return powers, true
	}
	if n == 1 {
		powers = append(powers, 0)
		return powers, true
	}
	pow := 1
	curr := 3
	for curr*3 <= n {
		curr *= 3
		pow++
	}
	subans, noRepeat := getPowersOfThree(n - curr)
	subans = append([]int{pow}, subans...)
	if len(subans) > 1 && pow == subans[1] {
		return subans, false
	}
	return subans, noRepeat
}

// @leet end
