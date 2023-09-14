#
# @lc app=leetcode id=1235 lang=python3
#
# [1235] Maximum Profit in Job Scheduling
#

# @lc code=start
from functools import lru_cache
import bisect


class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        # top down dp
        # sort a job by start time
        # for a new job either include it or skip it
        jobs = []
        for i in range(len(startTime)):
            jobs.append((startTime[i], endTime[i], profit[i]))
        jobs.sort(key=lambda x: x[0])
        sortedStart = [x[0] for x in jobs]

        @lru_cache(None)
        def maxProfit(idx):
            if idx >= len(startTime):
                return 0

            # skip or include
            skip = maxProfit(idx + 1)
            _, end, profit = jobs[idx]
            nextIdx = bisect.bisect_left(sortedStart, end)
            include = maxProfit(nextIdx) + profit
            return max(skip, include)

        return maxProfit(0)


# @lc code=end
