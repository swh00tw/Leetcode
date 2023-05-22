#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#

# @lc code=start
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.getString(s)==self.getString(t)
       
    def getString(self, s: str):
        stack=[]
        for char in list(s):
            if char=="#":
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        return "".join(stack)

      
        
# @lc code=end

