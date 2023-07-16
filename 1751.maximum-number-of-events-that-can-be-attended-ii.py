#
# @lc app=leetcode id=1751 lang=python3
#
# [1751] Maximum Number of Events That Can Be Attended II
#


# @lc code=start
from functools import lru_cache


class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # top down dp
        # sort the array first (bcz we need to traverse from earliest and do binary search next)
        events = list(sorted(events, key=lambda x: x[0]))
        n = len(events)

        @lru_cache(None)
        def dfs(i, j):
            # base case
            if i >= n or i < 0 or j == 0:
                return 0

            # option 1: choose the event, and find next available event by binary search
            nextEventIdx = self.binarySearch(events, events[i][1])
            answer1 = events[i][2] + dfs(nextEventIdx, j - 1)
            # option 2: skip this event
            answer2 = dfs(i + 1, j)

            answer = max(answer1, answer2)
            return answer

        return dfs(0, k)

    def binarySearch(self, events, val):
        l, r = 0, len(events) - 1
        while l <= r:
            mid = (l + r) // 2
            startTime = events[mid][0]
            if startTime > val:
                r = mid - 1
            else:
                l = mid + 1
        return l


# @lc code=end
