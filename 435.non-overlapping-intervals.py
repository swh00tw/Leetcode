#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#


# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort by end time (activity-selection problem)
        intervals = sorted(list(map(lambda x: (x[1], x[0]), intervals)))
        count = 0
        currEndTime = intervals[0][0]
        for end, start in intervals[1:]:  # the first item is already included
            if start >= currEndTime:  # include it
                currEndTime = end
            else:
                count += 1
        return count


# @lc code=end
