#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#


# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # dp[i][j] means number of unique paths to (i, j)
        # if (i, j) is an obstacle, dp[i][j] = 0
        # dp[i][j] = dp[i][j-1] + dp[i-1][j]
        # base case: if i==0 or j==0, dp[i][j]=1
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp = [[0] * m for _ in range(n)]
        for i in range(n):
            if obstacleGrid[i][0] != 0:
                break
            dp[i][0] = 1
        for j in range(m):
            if obstacleGrid[0][j] != 0:
                break
            dp[0][j] = 1
        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]


# @lc code=end
