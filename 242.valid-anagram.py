#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # parse s first, dictionary[char] = # of appearance of that char in string s
        # parse t to checl if they use same char set and the number of appearance is the same
        charDict = {}
        for c in s:
            if charDict.get(c):
                charDict[c] = charDict[c]+1
            else:
                charDict[c]=1
        for c in t:
            if charDict.get(c):
                charDict[c] = charDict[c]-1
            else:
                return False
        
        for key in charDict:
            if charDict[key]!=0:
                return False
        return True
        
        
        
# @lc code=end

