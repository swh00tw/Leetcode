#
# @lc app=leetcode id=1140 lang=python3
#
# [1140] Stone Game II
#

# @lc code=start
# ref: https://leetcode.com/problems/stone-game-ii/solutions/3563326/python-java-c-simple-solution-easy-to-understand/
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # 2-d dp problem
        # create a dp table: dp
        # dp[i][j] means the maximum stones alice or bob can get from index i if m=j
        # we also need to create a suffixSum table to improve time complexity
        # suffixSum[i] means the total stones we can get from index i
        # the optimal substructure of dp[i][j]
        # iterate through all possible x for alice
        # if there's remaining piles, iterate through all possible x for bob (the stones alice can't take)
        # then the optimal answer if suffixSum[i]-(the maximum stones for bob to get from derived position, which need to use dp table)
        # order of filling dp table: i-->backward(n-1 to 0), m-->start from 1 (1 to n)
        n = len(piles)
        dp = [[0]*(n+1) for _ in range(n)]
        suffixSum = [0]*n
        for i in range(n-1, -1, -1):
            suffixSum[i] = piles[i] + (suffixSum[i+1] if i+1<n else 0)
        
        # dp
        for i in range(n-1, -1, -1):
            for m in range(1, n+1):
                for x in range(1, 2*m+1):
                    if i+x >= n: # no remaining piles for opponent
                        dp[i][m] = suffixSum[i]
                    else:
                        opponentBestScore = dp[i+x][max(m, x)] # one's best score from index i+x
                        bestScore = suffixSum[i]-opponentBestScore # minus subproblem's optimal answer
                        dp[i][m] = max(dp[i][m], bestScore)
        return dp[0][1]
        
        
# @lc code=end

