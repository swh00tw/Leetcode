package main

// @leet start
func minimumOperations(nums []int) int {
	// maintain a variable distinctNums: the number of distinct nums
	// maintain a hashmap map from num to freq
	freq := make(map[int]int)
	for _, n := range nums {
		freq[n]++
	}
	distinctNums := 0
	for _, v := range freq {
		if v == 1 {
			distinctNums++
		}
	}
	iter := 0
	for len(nums) > distinctNums {
		if len(nums) == 0 {
			break
		}
		// remove first 3 nums
		// update freq, distinctNums
		for i := 0; i < 3; i++ {
			// pop the first element
			if len(nums) == 0 {
				break
			}
			first := nums[0]
			freq[first]--
			if freq[first] == 1 {
				distinctNums++
			} else if freq[first] == 0 {
				distinctNums--
			}
			nums = nums[1:]
		}
		iter++
	}
	return iter
}

// @leet end

