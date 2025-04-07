package main

// @leet start

// sol: https://leetcode.com/problems/partition-equal-subset-sum/solutions/6623686/0-1-knapsack-dp-with-images-example-walkthrough-c-python-java
func canPartition(nums []int) bool {
	sum := 0
	for _, num := range nums {
		sum += num
	}
	if sum%2 == 1 {
		return false
	}
	target := sum / 2
	canConstruct := make([]bool, target+1)
	canConstruct[0] = true
	for _, num := range nums {
		for i := target; i >= num; i-- {
			canConstruct[i] = canConstruct[i] || canConstruct[i-num]
		}
	}
	return canConstruct[target]
}

// @leet end

