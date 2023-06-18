#
# @lc app=leetcode id=2328 lang=python3
#
# [2328] Number of Increasing Paths in a Grid
#

# @lc code=start
class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        # TOP-DOWN DP
        m = len(grid[0])
        n = len(grid)
        deltas =[(0, 1), (1, 0), (-1, 0), (0, -1)]
        cache = [[-1]*m for _ in range(n)] # number of paths starting at (i,j)
        def countPathsEndAtCell(i, j, prev):
            if not (0<=i<n and 0<=j<m): # out of bound
                return 0
            if grid[i][j]<=prev: #
                return 0
            if cache[i][j]!=-1: # has calculated before
                return cache[i][j]
            ans = 1 # the cell has an answer itself
            for x, y in deltas:
                ans += countPathsEndAtCell(i+x, j+y, grid[i][j])
            # update cache and return
            cache[i][j] = ans
            return ans
        
        res = 0
        for i in range(n):
            for j in range(m):
                res += countPathsEndAtCell(i,j, -1)
        return res%(10**9+7)

        # BOTTOM-UP DP (34/36)
        # count how many k-length paths end at (i,j) for k in [1:m*n]
        # m = len(grid[0])
        # n = len(grid)
        # dp = [[1]*m for _ in range(n)] # dp[i][j] = how many valid paths end at (i,j)
        # ans = m*n
        # deltas =[(0, 1), (1, 0), (-1, 0), (0, -1)]
        # q = set([(i,j) for i in range(n) for j in range(m)]) # store the tails of the paths
        # for k in range(2, m*n+1):
        #     nextQ = set()
        #     nextDp = [[0]*m for _ in range(n)]
        #     newPaths = 0
        #     if len(q)==0:
        #         break
        #     for i, j in list(q):
        #         for x, y in deltas:
        #             if 0<=i+x<n and 0<=j+y<m and grid[i+x][j+y]>grid[i][j]:
        #                 nextDp[i+x][j+y]=(nextDp[i+x][j+y]+dp[i][j]) % (10**9+7)
        #                 nextQ.add((i+x, j+y))
        #                 newPaths += dp[i][j]
        #     if newPaths==0:
        #         break
        #     ans = (ans+newPaths)%(10**9+7)
        #     dp = nextDp
        #     q = nextQ
        # return ans
        
# @lc code=end

