#
# @lc app=leetcode id=452 lang=python3
#
# [452] Minimum Number of Arrows to Burst Balloons
#


# @lc code=start
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # interval schedling problem to find non-overlapping intervals
        # for overlapping intervals, we can ignore it since we can clear those balloons by shooting other balloons
        sorted_points = sorted(points, key=lambda x: x[1])
        intervals = [sorted_points[0]]
        for p in sorted_points[1:]:
            if p[0] <= intervals[-1][1]:
                continue
            else:
                intervals.append(p)
        return len(intervals)


# @lc code=end
