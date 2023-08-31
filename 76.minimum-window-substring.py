#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # sliding window on s
        # each time increment right pointer's index by one
        # if it encounter a letter not in the counter, skip
        # if it encounter a letter in the counter
        # include it
        # if we find a valid substring
        # try shrink it by moving left pointer until the substring is invalid
        # by doing so, we check every possible substring!
        m = len(s)
        left = 0
        freq = Counter(t)
        substringFreq = defaultdict(int)
        need = len(freq)  # how many letters we need to collect
        have = 0  # how many letters we finish collecting, plus one when we finish collecting one charactar
        ans = None
        for right in range(m):
            letter = s[right]
            substringFreq[letter] += 1
            # when we finish collecting a letter
            if freq.get(letter, -1) == substringFreq[letter]:
                have += 1
            # if we find a valid substring, try to shrink it
            while have == need and left <= right:
                if ans is None or right + 1 - left < len(ans):
                    ans = s[left : right + 1]
                if substringFreq[s[left]] == freq.get(s[left], -1):
                    have -= 1
                substringFreq[s[left]] -= 1
                left += 1
        return "" if ans is None else ans


# @lc code=end
