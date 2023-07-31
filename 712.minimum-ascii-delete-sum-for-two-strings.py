#
# @lc app=leetcode id=712 lang=python3
#
# [712] Minimum ASCII Delete Sum for Two Strings
#


# @lc code=start
class Solution:
    def __init__(self):
        self.cache = {}

    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # recursive
        # base case
        if len(s1) == 0:
            return self.toASCII(s2)
        elif len(s2) == 0:
            return self.toASCII(s1)
        if (s1, s2) in self.cache:
            return self.cache[(s1, s2)]

        if s1[-1] == s2[-1]:
            return self.minimumDeleteSum(s1[:-1], s2[:-1])
        else:
            ans = min(
                self.minimumDeleteSum(s1[:-1], s2) + ord(s1[-1]),
                self.minimumDeleteSum(s1, s2[:-1]) + ord(s2[-1]),
            )
            self.cache[(s1, s2)] = ans
            return ans

    def toASCII(self, s: str) -> int:
        c = 0
        for char in s:
            c += ord(char)
        return c


# @lc code=end
