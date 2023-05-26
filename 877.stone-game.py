#
# @lc app=leetcode id=877 lang=python3
#
# [877] Stone Game
#

# @lc code=start
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # 2-d dp problem
        # we can reduce the problem to maximize a value (imagine alice pick to plus, bob pick to minus)
        # optimal answer of piles[0, n-1] can be derived from 4 subproblem
        # l: leftmost, r: rightmost
        # (alice pick, bob pick) = (l, l), (l, r), (r, r), (r, l) + the optimal value from subproblem
        # base condition: if piles.length = 0, return 0
        n = len(piles)
        dp = [[0]*(n+1) for _ in range(n+1)]
        for x in range(1, n+1):
            if x%2==1:
                continue
            for i in range(n+1-x):
                j = x+i
                subpiles = piles[i:j]
                # (l, l)
                ll = subpiles[0]-subpiles[1]+dp[i+2][j]
                # (l, r)
                lr = subpiles[0]-subpiles[-1]+dp[i+1][j-1]
                # (r, r)                
                rr = subpiles[-1]-subpiles[-2]+dp[i][j-2]
                # (r, l)
                rl = subpiles[-1]-subpiles[0]+dp[i+1][j-1]
                dp[i][j] = max(rr, rl, ll, lr)
        return dp[0][n] > 0
# @lc code=end

