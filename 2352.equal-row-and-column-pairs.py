#
# @lc app=leetcode id=2352 lang=python3
#
# [2352] Equal Row and Column Pairs
#

# @lc code=start
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        ans = 0
        n = len(grid)
        rows = {}
        for row in grid:
            rows[tuple(row)] = rows.get(tuple(row), 0)+1
        # transpose
        for j in range(n):
            col = []
            for i in range(n):
                col.append(grid[i][j])
            ans += rows.get(tuple(col), 0)
        return ans
        
# @lc code=end

