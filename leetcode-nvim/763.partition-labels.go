package main

// @leet start
func partitionLabels(s string) []int {
	if len(s) == 0 {
		return []int{}
	}
	// for each letter, store [startIdx, endIdx]
	letterStartEndIndice := make(map[byte][]int)
	for i, b := range s {
		if _, ok := letterStartEndIndice[byte(b)]; !ok {
			letterStartEndIndice[byte(b)] = []int{i, i}
		} else {
			letterStartEndIndice[byte(b)][1] = i
		}
	}
	ans := []int{}
	l := 0
	r := 0
	n := len(s)
	for l < n {
		endIdx := letterStartEndIndice[s[l]][1]
		for r < n {
			endIdx = max(endIdx, letterStartEndIndice[s[r]][1])
			r++
			if r > endIdx {
				break
			}
		}
		ans = append(ans, r-l)
		l = r
	}
	return ans
}

// @leet end
