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
	r := 0
	n := len(s)
	endIdx := letterStartEndIndice[s[0]][1]
	for r < n {
		endIdx = max(endIdx, letterStartEndIndice[s[r]][1])
		r++
		if r > endIdx {
			break
		}
	}
	subans := partitionLabels(s[r:])
	return append([]int{r}, subans...)
}

// @leet end

