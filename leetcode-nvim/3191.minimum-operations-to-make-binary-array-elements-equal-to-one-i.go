package main

// @leet start
func minOperations(nums []int) int {
	// greedy
	zeros := 0
	for _, n := range nums {
		if n == 0 {
			zeros++
		}
	}
	if zeros == 0 {
		return 0
	}
	ops := 0
	idx := 0
	for idx+2 < len(nums) {
		if nums[idx] == 0 {
			for i := idx; i < idx+3; i++ {
				if nums[i] == 0 {
					nums[i] = 1
					zeros--
				} else {
					nums[i] = 0
					zeros++
				}
			}
			ops++
		}
		idx++
	}
	if zeros == 0 {
		return ops
	}
	return -1
}

// @leet end

