#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#


# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        n = len(s)
        unique = [True] * n  # unique[i] is True -> i is unique index
        seen = {}  # map char to idx
        for i, c in enumerate(s):
            if c in seen:
                unique[seen[c]] = False
                unique[i] = False
            seen[c] = i
        if not any(unique):
            return -1
        for i in range(n):
            if unique[i]:
                return i


# @lc code=end
