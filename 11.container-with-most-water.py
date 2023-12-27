#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#


# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # two pointers
        l, r = 0, len(height) - 1
        best = float("-inf")
        while l < r:
            best = max(best, (r - l) * min(height[r], height[l]))
            if height[r] <= height[l]:
                r -= 1
            else:
                l += 1
        return best


# @lc code=end
