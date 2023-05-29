#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxHeight = max(height)
        l, r = 0, len(height)-1
        best = 0
        while l<r:
            if height[l]==maxHeight and height[r]==maxHeight:
                best = max(best, (r-l)*(maxHeight))
                break
            best = max(best, (r-l)*min(height[l], height[r]))
            if height[r]<height[l]:
                r-=1
            else:
                l+=1
        return best
# @lc code=end

