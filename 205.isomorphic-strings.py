#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        wordMap={}
        wordBeenMap={}
        for i in range(len(s)):
            letter1 = s[i]
            letter2 = t[i]

            if wordMap.get(letter1) and letter2 != wordMap[letter1]:
                return False
            elif wordBeenMap.get(letter2) and letter1 != wordBeenMap[letter2]:
                return False
            else:
                wordMap[letter1]=letter2
                wordBeenMap[letter2]=letter1

        return True
        
# @lc code=end

