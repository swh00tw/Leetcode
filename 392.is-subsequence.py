#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        criterionQueue = list(s)
        for letter in t:
            if len(criterionQueue)==0:
                break
            requiredLetter = criterionQueue[0]
            if letter == requiredLetter:
                del criterionQueue[0]
        return len(criterionQueue)==0 
        
# @lc code=end

