package main

// @leet start
func minDominoRotations(tops []int, bottoms []int) int {
	// aim to make top the same, if k operations and the length is n, the answer is min(k, n-k)
	// for each number, count how many indices the number appears in tops or bottoms
	// if no number appears n times, return -1
	// then we have the numbers that appears exactly n times,
	// we need to pick the one that need the least operations
	// --> the number that distribute the most unevenly
	freq := make(map[int][]int) // for each number, track number of indices, occurence in tops and bottoms
	n := len(tops)
	for i := 0; i < n; i++ {
		if freq[tops[i]] == nil {
			freq[tops[i]] = make([]int, 3)
		}
		if freq[bottoms[i]] == nil {
			freq[bottoms[i]] = make([]int, 3)
		}
		if tops[i] == bottoms[i] {
			freq[tops[i]][0]++
			freq[tops[i]][1]++
			freq[tops[i]][2]++
		} else {
			freq[tops[i]][0]++
			freq[tops[i]][1]++
			freq[bottoms[i]][0]++
			freq[bottoms[i]][2]++
		}
	}
	candidates := []int{}
	for k, v := range freq {
		if v[0] == n {
			candidates = append(candidates, k)
		}
	}
	if len(candidates) == 0 {
		return -1
	}

	bestAns := []int{-1, n} // the number, the number of operations
	for _, k := range candidates {
		overlapped := freq[k][1] + freq[k][2] - n
		ops := min(freq[k][1], freq[k][2]) - overlapped
		if ops < bestAns[1] {
			bestAns[0] = k
			bestAns[1] = ops
		}
	}
	return bestAns[1]
}

// @leet end

