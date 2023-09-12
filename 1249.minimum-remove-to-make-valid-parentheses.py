#
# @lc app=leetcode id=1249 lang=python3
#
# [1249] Minimum Remove to Make Valid Parentheses
#


# @lc code=start
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = 0
        LEFT = "("
        RIGHT = ")"
        EMPTY = "."
        s = list(s)
        for i, c in enumerate(s):
            if c == LEFT:
                stack += 1
            elif c == RIGHT:
                if stack == 0:
                    s[i] = EMPTY
                else:
                    stack -= 1
        r = len(s) - 1
        while stack > 0:
            if s[r] == LEFT:
                s[r] = EMPTY
                stack -= 1
            r -= 1
        res = list(filter(lambda x: x != EMPTY, s))
        return res


# @lc code=end
