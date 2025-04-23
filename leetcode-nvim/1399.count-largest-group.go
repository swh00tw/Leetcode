package main

// @leet start
func countLargestGroup(n int) int {
	// create a hashmap map the sum of digits to group members
	// after constructing, create another hashmap map the size of group to number of groups
	sumToMembers := make(map[int][]int)
	getSum := func(n int) int {
		ans := 0
		for n > 0 {
			ans += n % 10
			n /= 10
		}
		return ans
	}
	for i := 1; i <= n; i++ {
		sum := getSum(i)
		if _, ok := sumToMembers[sum]; !ok {
			sumToMembers[sum] = []int{}
		}
		sumToMembers[sum] = append(sumToMembers[sum], i)
	}

	maxKey := 0
	sizeToCount := make(map[int]int)
	for _, v := range sumToMembers {
		length := len(v)
		sizeToCount[length]++
		if length > maxKey {
			maxKey = length
		}
	}
	return sizeToCount[maxKey]
}

// @leet end

