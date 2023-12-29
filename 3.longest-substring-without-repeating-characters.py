#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#


# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # maintain a set within sliding window
        chars = set()
        startIdx = 0
        best = 0
        for endIdx in range(len(s)):
            newChar = s[endIdx]
            if newChar in chars:
                # shrink startIdx
                # until popping out the same charactar
                while s[startIdx] != newChar:
                    chars.discard(s[startIdx])
                    startIdx += 1
                chars.discard(s[startIdx])
                startIdx += 1

            # update best
            best = max(best, endIdx + 1 - startIdx)
            # update chars
            chars.add(newChar)
        return best


# @lc code=end
