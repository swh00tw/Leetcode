#
# @lc app=leetcode id=790 lang=python3
#
# [790] Domino and Tromino Tiling
#

# @lc code=start
# ref: https://leetcode.com/problems/domino-and-tromino-tiling/description/comments/1566271
class Solution:
    def numTilings(self, n: int) -> int:
        # dp[1] = 1, dp[2] = 2, dp[3] = 1+2*(dp[2]-1)+(form by tromino)
        if n==1:
            return 1
        if n==2:
            return 2
        if n==3:
            return 5
        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 2
        dp[3] = 5
        for i in range(4, n+1):
            dp[i] = 2*dp[i-1]+dp[i-3]
        return dp[n]%(10**9+7)
        
# @lc code=end

