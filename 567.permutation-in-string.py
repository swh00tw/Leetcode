#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # each time move right pointer by one
        # each reach an char not in s1Char, reset left pointer to right pointer
        # each count for a char is zero, recycle that char (move left pointer)
        s1Char = Counter(s1)
        n = len(s2)
        startIdx = 0
        for endIdx in range(n):
            newChar = s2[endIdx]
            # if meet a char that is not in s1, reset everything
            if newChar not in s1Char:
                s1Char = Counter(s1)
                startIdx = endIdx + 1
            else:
                # if meet a char and we can keep counting
                if s1Char[newChar] > 0:
                    s1Char[newChar] -= 1
                    if endIdx + 1 - startIdx == len(s1):
                        return True
                # if meet a char but the count for that char is zero
                # move the left pointer to recycle chars, until reach a char that equal the newChar
                else:
                    while s2[startIdx] != newChar:
                        s1Char[s2[startIdx]] += 1
                        startIdx += 1
                    startIdx += 1
        return False


# @lc code=end
