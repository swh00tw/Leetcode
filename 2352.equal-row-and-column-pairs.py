#
# @lc app=leetcode id=2352 lang=python3
#
# [2352] Equal Row and Column Pairs
#

# @lc code=start
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        ans = 0
        rows = {}
        for row in grid:
            rows[tuple(row)] = rows.get(tuple(row), 0)+1
        # transpose
        transposeGrid=zip(*grid)
        for col in transposeGrid:
            ans += rows.get(col, 0)
        return ans
        
# @lc code=end

