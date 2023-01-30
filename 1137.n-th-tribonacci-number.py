#
# @lc app=leetcode id=1137 lang=python3
#
# [1137] N-th Tribonacci Number
#

# @lc code=start
class Solution:
    def tribonacci(self, n: int) -> int:
        tribonaccis = [0,1,1]
        if n < 3:
            return tribonaccis[n]
        
        for i in range(3, n+1):
            next = tribonaccis[i-1]+tribonaccis[i-2]+tribonaccis[i-3]
            tribonaccis.append(next)
        return tribonaccis[-1]
# @lc code=end

