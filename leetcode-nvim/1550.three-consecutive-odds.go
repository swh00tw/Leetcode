package main

// @leet start
func threeConsecutiveOdds(arr []int) bool {
	n := len(arr)
	i := 0
	for i < n {
		if arr[i]%2 == 1 {
			if i+2 < n && arr[i+1]%2 == 1 && arr[i+2]%2 == 1 {
				return true
			}
		}
		i++
	}
	return false
}

// @leet end

