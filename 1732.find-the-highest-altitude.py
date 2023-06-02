#
# @lc app=leetcode id=1732 lang=python3
#
# [1732] Find the Highest Altitude
#

# @lc code=start
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        currHeight = 0
        res = 0
        for g in gain:
            currHeight += g
            res = max(res, currHeight)
        return res
        
# @lc code=end

