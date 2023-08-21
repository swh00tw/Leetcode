#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#


# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        startIdx = 0
        ans = 0
        chars = set()
        for endIdx, c in enumerate(s):
            newChar = s[endIdx]
            if newChar in chars:
                # move startIdx until the conflict resolve
                while s[startIdx] != newChar:
                    chars.remove(s[startIdx])
                    startIdx += 1
                chars.remove(s[startIdx])
                startIdx += 1
            chars.add(newChar)
            ans = max(ans, endIdx + 1 - startIdx)
        return ans


# @lc code=end
