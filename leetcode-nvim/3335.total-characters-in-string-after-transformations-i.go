package main

// @leet start
// ref: https://leetcode.com/problems/total-characters-in-string-after-transformations-i/solutions/6735769/total-characters-in-string-after-transformations-i
const mod = 1000000007

func lengthAfterTransformations(s string, t int) int {
	cnt := make([]int, 26)
	for _, ch := range s {
		cnt[ch-'a']++
	}
	for round := 0; round < t; round++ {
		nxt := make([]int, 26)
		nxt[0] = cnt[25]
		nxt[1] = (cnt[25] + cnt[0]) % mod
		for i := 2; i < 26; i++ {
			nxt[i] = cnt[i-1]
		}
		cnt = nxt
	}
	ans := 0
	for i := 0; i < 26; i++ {
		ans = (ans + cnt[i]) % mod
	}
	return ans
}

// @leet end

