#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        left = set(["[", "{", "("])
        stack = []
        for p in s:
            if p in left:
                stack.append(p)
            else:
                if len(stack)==0:
                    return False
                tmp = ''.join([stack[-1], p])
                if tmp=="()" or tmp=="{}" or tmp=="[]":
                    stack.pop(-1)
                else:
                    return False
        return len(stack)==0  
        
# @lc code=end

