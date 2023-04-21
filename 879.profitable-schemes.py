#
# @lc app=leetcode id=879 lang=python3
#
# [879] Profitable Schemes
#

# @lc code=start
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        # create dp table, dp[i][j] means # of ways to earn exact profit j using i people
        dp = [[0]*(minProfit+1) for _ in range(n+1)]
        dp[0][0] = 1

        # update 2d table len(group) times
        res = 0
        # each iteration means new task appear and we decide to pick the new task
        for reqWorkers, gain in zip(group, profit): 
            for i in range(n, 0, -1):
                if i >= reqWorkers:
                    for p in range(minProfit+1):
                        if p + gain >= minProfit:
                            dp[i][minProfit] += dp[i-reqWorkers][p]
                            res += dp[i-reqWorkers][p]
                        else:
                            dp[i][p+gain] += dp[i-reqWorkers][p]
        
        return (res if minProfit>0 else res+1)%(10**9+7)
# @lc code=end

