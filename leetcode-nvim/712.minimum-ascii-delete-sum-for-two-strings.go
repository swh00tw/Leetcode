package main

// @leet start
func minimumDeleteSum(s1 string, s2 string) int {
	// n = len(s1), m = len(s2)
	// ans[n][m] is final answer
	// ans[x][y] is the ans for s1[:x], s2[:y]
	// ans[x][y] = if s1[x-1] == s2[y-1] then ans[x-1][y-1]
	// if s1[x-1] != s2[y-1] then
	// throw away s2[y-1], ascii(s2[y-1])+ans[x][y-1]
	// throw away s1[x-1], ascii(s1[x-1])+ans[x-1][y]
	// base case:
	// if x == 0 || y == 0, then ans is the sum of ascii value of the other string

	cache := map[[2]int]int{}
	var getAns func(x, y int) int
	getAns = func(x, y int) int {
		if x == 0 && y == 0 {
			return 0
		}
		if x == 0 {
			ans := 0
			for _, c := range s2[:y] {
				ans += int(c)
			}
			return ans
		}
		if y == 0 {
			ans := 0
			for _, c := range s1[:x] {
				ans += int(c)
			}
			return ans
		}

		key := [2]int{x, y}
		if val, ok := cache[key]; ok {
			return val
		}
		ans := min(int(s2[y-1])+getAns(x, y-1), int(s1[x-1])+getAns(x-1, y))
		if s1[x-1] == s2[y-1] {
			ans = min(ans, getAns(x-1, y-1))
		}

		cache[key] = ans
		return ans
	}

	return getAns(len(s1), len(s2))
}

// @leet end

