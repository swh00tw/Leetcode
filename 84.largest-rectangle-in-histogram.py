#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#


# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # for each element, it want to expand to its left and right as many as possible
        # therefore, for each element, find the boundary it can expand to left and right
        # find nearest smaller element at left and nearest smaller element at right
        # using stack to find nearest smallest to left and right
        n = len(heights)
        nearestSmallerLeft = [0] * n
        nearestSmallerRight = [0] * n
        # calculate for left
        helperStack = []
        for i in range(n):
            currHeight = heights[i]
            while len(helperStack) > 0 and helperStack[-1][0] >= currHeight:
                helperStack.pop()
            if not helperStack:
                nearestSmallerLeft[i] = -1
            else:
                nearestSmallerLeft[i] = helperStack[-1][1]
            helperStack.append((currHeight, i))
        # calculate for right
        helperStack = []
        for i in range(n - 1, -1, -1):
            currHeight = heights[i]
            while len(helperStack) > 0 and helperStack[-1][0] >= currHeight:
                helperStack.pop()
            if not helperStack:
                nearestSmallerRight[i] = n
            else:
                nearestSmallerRight[i] = helperStack[-1][1]
            helperStack.append((currHeight, i))

        best = -inf
        for i in range(n):
            height = heights[i]
            width = (nearestSmallerRight[i] - nearestSmallerLeft[i]) - 1
            best = max(best, height * width)
        return best


# @lc code=end
