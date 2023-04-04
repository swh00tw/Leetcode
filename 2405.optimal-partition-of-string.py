#
# @lc app=leetcode id=2405 lang=python3
#
# [2405] Optimal Partition of String
#

# @lc code=start
class Solution:
    def partitionString(self, s: str) -> int:
        if len(s)==0: 
            return 0
        res = 0
        charSet = set()
        for char in s:
            if char in charSet:
                charSet = set()
                res +=1
            charSet.add(char)
        if charSet:
            res+=1
        return res
        
            

        
# @lc code=end

