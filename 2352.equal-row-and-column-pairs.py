#
# @lc app=leetcode id=2352 lang=python3
#
# [2352] Equal Row and Column Pairs
#

# @lc code=start
from collections import defaultdict


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # brute force: n^3
        # hashmap: use row as key (need to transform to tuple since list is not hashable), value is the frequency
        freq = defaultdict(int)
        n = len(grid)
        for row in grid:
            freq[tuple(row)] += 1
        # transpose
        ans = 0
        transpose_grid = [[grid[j][i] for j in range(n)] for i in range(n)]
        for row in transpose_grid:
            if tuple(row) in freq:
                ans += freq[tuple(row)]
        return ans


# @lc code=end
