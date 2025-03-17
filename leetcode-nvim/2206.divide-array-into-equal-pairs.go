package main

// @leet start
func divideArray(nums []int) bool {
	// use a map to track
	// if a number is not in hashmap, add it,
	// else, delete the key,
	// in the end, return true if the map is empty
	numsMap := make(map[int]bool)
	for _, n := range nums {
		if _, ok := numsMap[n]; !ok {
			numsMap[n] = true
		} else {
			delete(numsMap, n)
		}
	}
	return len(numsMap) == 0
}

// @leet end
