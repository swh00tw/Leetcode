#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp[i] means the min cost to arrive i step
        # ex: dp[3] when cost=[10, 15, 20] equal to 15, dp[0]=0, dp[1]=0, dp[2]=min(10, 15)
        # dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        n = len(cost)
        dp = [0]*n
        for i in range(2, n):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        return min(dp[-1]+cost[-1], dp[-2]+cost[-2])         

# @lc code=end

