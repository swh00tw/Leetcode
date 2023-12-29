#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
from collections import deque


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # overlapped: (a,b), (c,d) if c<=b
        # sort by starting time
        # keep popping
        # TC: O(nlgn)
        intervals.sort()
        queue = deque(intervals)
        ans = []
        ans.append(queue.popleft())
        while queue:
            newInterval = queue.popleft()
            c, d = newInterval
            _, b = ans[-1]
            if c <= b:
                # merge
                ans[-1][1] = max(d, b)
            else:
                ans.append([c, d])
        return ans


# @lc code=end
