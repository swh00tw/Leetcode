#
# @lc app=leetcode id=1456 lang=python3
#
# [1456] Maximum Number of Vowels in a Substring of Given Length
#

# @lc code=start
def isVowel(char):
    if len(char)>1:
        raise Exception("isVowel's input should be one char")
    vowels = "aeiou"
    return char in vowels
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        i = 0
        window = s[i:i+k]
        count = 0
        for c in window:
            if isVowel(c):
                count+=1
        best = count
        i+=1
        while i<len(s) and i+k<=len(s):
            count += (1 if isVowel(s[i+k-1]) else 0)
            count -= (1 if isVowel(s[i-1]) else 0)
            best = max(best, count)
            i+=1
        return best
        
        
# @lc code=end

