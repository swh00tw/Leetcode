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
        points = list(sorted(points, key=lambda x: x[1]))
        count = 0
        currEndTime = points[0][1]
        for start, end in points[1:]:
            if start > currEndTime:
                currEndTime = end
            else:
                count += 1
        return len(points) - count


# @lc code=end
