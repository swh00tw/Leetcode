#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
from collections import defaultdict, Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        m = len(p)
        if n<m:
            return []
        charMap = Counter(p)
        ans = []
        # search s[0:m]
        for i in range(m):
            if s[i] in charMap:
                charMap[s[i]]-=1 
        # use sliding window  
        for i in range(n-m+1):
            if all(x==0 for x in charMap.values()):
                ans.append(i)
            # right shift
            if s[i] in charMap:
                charMap[s[i]]+=1
            if i+m < n and s[i+m] in charMap:
                charMap[s[i+m]]-=1
        return ans
        
# @lc code=end

