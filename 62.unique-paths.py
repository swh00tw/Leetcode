#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # C (m+n-2) pick n-1
        return math.comb(m+n-2, m-1)
        
# @lc code=end

