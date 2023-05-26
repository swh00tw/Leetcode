#
# @lc app=leetcode id=2390 lang=python3
#
# [2390] Removing Stars From a String
#

# @lc code=start
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for c in s:
            if c=="*":
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)
        
# @lc code=end

