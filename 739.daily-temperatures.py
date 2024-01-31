#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#


# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # maintain a stack, and the temperature inside only gets lower or equal
        # store (tempature, index) inside
        # when parse a new tempature, try push it into stack
        # pop and process if the top one is cooler
        stack = []
        n = len(temperatures)
        ans = [0] * n
        for idx, temp in enumerate(temperatures):
            # push
            while stack and stack[-1][0] < temp:
                _, targetIdx = stack.pop()
                ans[targetIdx] = idx - targetIdx
            stack.append((temp, idx))
        return ans


# @lc code=end
