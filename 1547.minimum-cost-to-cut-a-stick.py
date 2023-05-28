#
# @lc app=leetcode id=1547 lang=python3
#
# [1547] Minimum Cost to Cut a Stick
#

# @lc code=start
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        # 2d dp problem
        # create an array breakpoints = [0] + sorted(cuts) + [n] (m=len)
        # create a 2d table (m)x(m), dp[i][j] means the minCost to cut rod from breakpoint i to breakpoint j
        # the optimal substructure: dp[i][j] = min((breakpoint[j]-breakpoint[i])+(dp[i][breakpointM]+dp[breakpointM][j])) for each breakpointM between them
        # trivial solution: i=j or j-i = 1, dp[i][j] = 0
        breakpoints = [0] + sorted(cuts) + [n]
        m = len(breakpoints)
        dp = [[0]*m for _ in range(m)]
        for k in range(2, m):
            for i in range(m-k):
                j = k+i
                tmp = inf
                middleBreakpoint = i+1
                while middleBreakpoint<j:
                    tmp = min(tmp, breakpoints[j]-breakpoints[i]+dp[i][middleBreakpoint]+dp[middleBreakpoint][j])
                    middleBreakpoint+=1
                dp[i][j] = 0 if tmp == inf else tmp
        return dp[0][m-1]
        

        # 2d dp problem
        # create a 2d (n+1)x(n+1) table dp, dp[i][j] denote the minCost of cutting the sub-wood (wood[i:j]) given cuts
        # k = j-i, we need to iterate from k=2 to k=n
        # iterate through the cutting points between them, count the minCost of subproblem
        # dp[i][j] = (j-1) + dp[i, m] + dp[m, j]
        # we transform cuts array to bitmask of len n to know where is the cutting point between i & j
        # dp = [[0]*(n+1) for _ in range(n+1)]
        # for k in range(2, n+1):
        #     for i in range(n-k+1):
        #         j = i+k
        #         tmp = inf
        #         for cuttingPoint in cuts:
        #             if cuttingPoint>i and cuttingPoint<j:
        #                 tmp = min(tmp, (j-i)+dp[i][cuttingPoint]+dp[cuttingPoint][j])
        #         dp[i][j] = 0 if tmp == inf else tmp
        # return dp[0][n]


        
# @lc code=end

