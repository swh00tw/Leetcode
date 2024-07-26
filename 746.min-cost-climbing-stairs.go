/*
 * @lc app=leetcode id=746 lang=golang
 *
 * [746] Min Cost Climbing Stairs
 */

// @lc code=start
func minCostClimbingStairs(cost []int) int {
	minCost := make([]int, len(cost)+1)
	for i := 2; i <= len(cost); i++ {
		minCost[i] = min(minCost[i-1]+cost[i-1], minCost[i-2]+cost[i-2])
	}
	return minCost[len(cost)]
}

// @lc code=end

