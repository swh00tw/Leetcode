package main

// @leet start
func mostPoints(questions [][]int) int64 {
	cache := make(map[int]int64)

	var getAns func(int) int64
	getAns = func(i int) int64 {
		if v, ok := cache[i]; ok {
			return v
		}
		// base case
		if i == len(questions)-1 {
			return int64(questions[i][0])
		}
		if i >= len(questions) {
			return int64(0)
		}
		// general case, either take or skip
		ans := getAns(i + 1)
		take := int64(questions[i][0]) + getAns(i+questions[i][1]+1)
		if take > ans {
			ans = take
		}
		cache[i] = ans
		return ans
	}

	return getAns(0)
}

// @leet end

