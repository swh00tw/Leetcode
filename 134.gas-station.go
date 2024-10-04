/*
 * @lc app=leetcode id=134 lang=golang
 *
 * [134] Gas Station
 */

// @lc code=start
package main

// ref: https://leetcode.com/problems/gas-station/solutions/1706142/java-c-python-an-explanation-that-ever-exists-till-now
func canCompleteCircuit(gas []int, cost []int) int {
	totalSurplus := 0 // used for edge case, sum of the gas is less than sum of the cost

	n := len(gas)
	surplus := 0
	start := 0

	for i := 0; i < n; i++ {
		totalSurplus += gas[i] - cost[i]
		surplus += gas[i] - cost[i]
		if surplus < 0 {
			start = i + 1
			surplus = 0
		}
	}

	if totalSurplus < 0 {
		return -1
	}
	return start
}

// @lc code=end
