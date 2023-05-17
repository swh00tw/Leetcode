#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def __init__(self):
        self.res = []
    def generateParenthesis(self, n: int) -> List[str]:
        self.construct("", 0, 0, n)
        return self.res
    def construct(self, currentString, left, right, n):
        if len(currentString)==2*n:
            self.res.append(currentString)
            return
        if left < n:
            self.construct(currentString+"(", left+1, right, n)
        if right<left:
            self.construct(currentString+")", left, right+1, n)
# @lc code=end

