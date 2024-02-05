#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#


# @lc code=start
from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        n = len(s)
        freq = Counter(s)
        for i in range(n):
            if freq[s[i]] == 1:
                return i
        return -1


# @lc code=end
