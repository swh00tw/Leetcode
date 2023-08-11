#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # the speed must in the range between 1 to max(piles)
        # # find the min speed inside the range that satisfy the requirement
        l, r = 1, max(piles)
        while l <= r:
            mid = (l + r) // 2  # speed
            hours = 0
            for bananas in piles:
                hours += math.ceil(bananas / mid)
            if hours > h:
                l = mid + 1
            else:
                r = mid - 1
        return l


# @lc code=end
