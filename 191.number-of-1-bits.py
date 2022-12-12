#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        num = n
        res = 0
        while (num>0):
            remainder = num % (2)
            dividend = num // (2)
            num = dividend
            res += remainder
        return res
        
# @lc code=end

