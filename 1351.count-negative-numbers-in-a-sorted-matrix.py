#
# @lc app=leetcode id=1351 lang=python3
#
# [1351] Count Negative Numbers in a Sorted Matrix
#

# @lc code=start
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        n = len(grid)
        m = len(grid[0])
        i, j = 0, m-1 # curr
        # if curr is negative number, increment count and go to left block
        # else, go down
        # break until curr leave the grid
        while 0<=i<n and 0<=j<m:
            if grid[i][j]<0:
                count += (n-i)
                j -= 1
            else:
                i += 1
        return count

        
# @lc code=end

