package main

// @leet start
func numberOfSubstrings(s string) int {
	// two pointers, once in the window, at least one 'a', 'b', 'c'
	// the answer should increment by n - right, increment left by 1
	l, r := 0, 0
	ans := 0
	freq := make(map[byte]int)
	n := len(s)
	for r < n {
		char := s[r]
		freq[char]++
		for len(freq) == 3 {
			ans += n - r
			// move l
			removeChar := s[l]
			freq[removeChar]--
			if freq[removeChar] == 0 {
				delete(freq, removeChar)
			}
			l++
		}
		r++
	}
	return ans
}

// @leet end

