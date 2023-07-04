#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#


# @lc code=start
from collections import deque


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # store (temp, index) pair
        # the temp must in decreasing order
        ans = [0] * len(temperatures)
        stack = deque([])
        for i, temp in enumerate(temperatures):
            while len(stack) > 0 and stack[-1][0] < temp:
                _, waitDayIdx = stack.pop()
                ans[waitDayIdx] = i - waitDayIdx
            stack.append((temp, i))
        return ans


# @lc code=end
