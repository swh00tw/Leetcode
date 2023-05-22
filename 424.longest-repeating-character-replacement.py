#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
# ref: https://leetcode.com/problems/longest-repeating-character-replacement/solutions/3524144/python-code-explained-with-approach-and-time-complexity/
class Solution:
    def __init__(self):
        self.m = 0
    def characterReplacement(self, s: str, k: int) -> int:
        # init two pointers l, r to 0
        # create a var maxf record the maxFrequency in sliding window
        # create a dictionary d that count the freq of each chars in s[l:r+1]
        # increment r from 0 to len(s)-1
        # each time increment, update d and maxf
        # if (windowSize - maxf) > k: shrink by increment left pointer by 1
        l ,r = 0, 0
        maxf = 0
        n = len(s)
        d = {}
        for r in range(n):
            d[s[r]] = 1+d.get(s[r], 0)
            maxf = max(d.values())
            if (r-l+1)-maxf>k:
                d[s[l]]-=1
                l+=1
            self.m = max(self.m, r-l+1)
        return self.m


        
# @lc code=end

