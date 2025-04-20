package main

// @leet start
func numRabbits(answers []int) int {
	// if answer different number, they must be in different color,
	// if answer the same number, two cases,
	// they have the same color, or they have different color
	// to answer the minimum number of rabbits, we assume they have the same color by default,
	// until it doesn't make sense, ex, 3 rabbits answer 1,
	// use a hashmap to store freq
	freq := make(map[int]int)
	for _, num := range answers {
		freq[num]++
	}
	ans := 0
	for answer, v := range freq {
		perGroup := answer + 1
		groups := v / perGroup
		if v%perGroup != 0 {
			groups++
		}
		ans += groups * perGroup
	}
	return ans
}

// @leet end

