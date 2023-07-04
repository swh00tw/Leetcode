#
# @lc app=leetcode id=859 lang=python3
#
# [859] Buddy Strings
#

# @lc code=start
from collections import Counter


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        sChar = Counter(s)
        gChar = Counter(goal)
        if sChar != gChar:
            return False
        # the distance must be 2
        distance = 0
        for i in range(len(s)):
            if s[i] != goal[i]:
                distance += 1
        if distance == 2:
            return True
        elif distance > 2:
            return False
        # if the distance is zero, check if there's any char appear twice or more
        for v in sChar.values():
            if v >= 2:
                return True
        return False


# @lc code=end
