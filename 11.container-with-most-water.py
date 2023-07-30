#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#


# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # two pointers, each time, move lower one
        l, r = 0, len(height) - 1
        ans = -inf
        while l < r:
            ans = max(ans, (r - l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            elif height[r] < height[l]:
                r -= 1
            else:
                nl = height[l + 1]
                nr = height[r - 1]
                if nl > nr:
                    l += 1
                else:
                    r -= 1
        return ans


# @lc code=end
