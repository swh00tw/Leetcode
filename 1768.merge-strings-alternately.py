#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
#

# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        res = ""
        iter = max(len(word1), len(word2))
        while i<iter:
            res+=word1[i] if i<len(word1) else ""
            res+=word2[i] if i<len(word2) else ""
            i+=1
        return res
        
# @lc code=end

