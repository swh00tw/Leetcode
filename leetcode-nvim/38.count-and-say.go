package main

import "fmt"

// @leet start
func countAndSay(n int) string {
	if n == 1 {
		return "1"
	}
	prev := countAndSay(n - 1)

	// run length encoding
	rle := func(s string) string {
		if len(s) == 0 {
			return ""
		}
		res := ""
		count := 1
		curr := s[0]
		for i := 1; i < len(s); i++ {
			if s[i] == curr {
				count++
				continue
			}
			res += fmt.Sprintf("%d", count) + string(curr)
			count = 1
			curr = s[i]
		}
		res += fmt.Sprintf("%d", count) + string(curr)
		return res
	}
	return rle(prev)
}

// @leet end

