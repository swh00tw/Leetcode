#
# @lc app=leetcode id=443 lang=python3
#
# [443] String Compression
#

# @lc code=start
class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars)==1:
            return 1
        currChar=chars[0]
        breakpoints=[[0, currChar]] # [index, char] pair
        for i, char in enumerate(chars):
            if i==0:
                continue
            if char != currChar:
                breakpoints.append([i, char])
                currChar = char
        
        s=""
        for i, pair in enumerate(breakpoints):
            index, char = pair
            nextIndex = len(chars) if i==len(breakpoints)-1 else breakpoints[i+1][0]
            length = nextIndex-index
            s+=char
            if length>1:
                s+=str(length)
        
        for i in range(len(s)):
            chars[i]=s[i]

        return len(s)
            

        
# @lc code=end

