package main

import (
	"math"
)

// @leet start

var INF = math.MaxInt

func pushDominoes(dominoes string) string {
	// first pass, only look at R, for each ".", track the "pushed time" (for "L", the val is inf, for "R", the val is -1)
	// second pass, only look at L (for "R", the val is inf, for "L", the val is -1)
	// for each ".", if R time < L time, then it is pushed by R, otherwise by L
	// if equal, it stays upright
	n := len(dominoes)
	Rtime := make([]int, n) // the time when each domino is pushed by "R"
	Ltime := make([]int, n) // the time when each domino is pushed by "L"
	R_indices := []int{}    // rightmost indices of each "R" groups
	L_indices := []int{}    // leftmost indices of each "L" groups
	for i := 0; i < n; i++ {
		if dominoes[i] == 'R' {
			Rtime[i] = 0
			Ltime[i] = INF
		} else if dominoes[i] == 'L' {
			Rtime[i] = INF
			Ltime[i] = 0
		} else {
			Rtime[i] = INF
			Ltime[i] = INF
		}
	}
	R_curr := -1
	for i := 0; i < n; i++ {
		if dominoes[i] == 'R' {
			if i != R_curr+1 {
				if R_curr != -1 {
					R_indices = append(R_indices, R_curr)
				}
			}
			R_curr = i
		}
	}
	if R_curr != -1 {
		R_indices = append(R_indices, R_curr)
	}
	L_curr := n
	for i := n - 1; i >= 0; i-- {
		if dominoes[i] == 'L' {
			if i != L_curr-1 {
				if L_curr != n {
					L_indices = append(L_indices, L_curr)
				}
			}
			L_curr = i
		}
	}
	if L_curr != n {
		L_indices = append(L_indices, L_curr)
	}
	// fill R time
	for _, r_idx := range R_indices {
		curr_time := 1
		curr_idx := r_idx + 1
		for curr_idx < n && dominoes[curr_idx] == '.' {
			Rtime[curr_idx] = curr_time
			curr_idx++
			curr_time++
		}
	}
	// fill L time
	for _, l_idx := range L_indices {
		curr_time := 1
		curr_idx := l_idx - 1
		for curr_idx >= 0 && dominoes[curr_idx] == '.' {
			Ltime[curr_idx] = curr_time
			curr_idx--
			curr_time++
		}
	}
	final := make([]byte, n)
	for i := 0; i < n; i++ {
		if Rtime[i] < Ltime[i] {
			final[i] = 'R'
		} else if Rtime[i] > Ltime[i] {
			final[i] = 'L'
		} else {
			final[i] = '.'
		}
	}
	return string(final)
}

// @leet end

