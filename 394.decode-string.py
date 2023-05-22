#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char!=']':
                stack.append(char)
            else:
                stringInside = ""
                multiplier = None
                while multiplier is None:
                    c = stack.pop()
                    if c=='[':
                        multiplier = ""
                        while stack:
                            if stack[-1].isdigit():
                                multiplier = stack.pop()+multiplier
                            else:
                                break
                        multiplier = int(multiplier)
                    else:
                        stringInside = c + stringInside
                stack = stack+list(multiplier*stringInside)
        return ''.join(stack)
        
# @lc code=end

