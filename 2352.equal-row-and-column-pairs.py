#
# @lc app=leetcode id=2352 lang=python3
#
# [2352] Equal Row and Column Pairs
#

# @lc code=start
from collections import defaultdict
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rows = {}
        cols = defaultdict(list)
        for i, row in enumerate(grid):
            rows[i] = row
            for j in range(n):
                cols[j].append(row[j])
        pairs = set()
        for i in range(n):
            for j in range(n):
                if rows[i]==cols[j] and (i,j) not in pairs:
                    pairs.add((i,j))
        return len(pairs)
        
        
# @lc code=end

