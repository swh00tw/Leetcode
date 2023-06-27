#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # use XOR operation since two identical number XOR together will be 0
        # and any number XOR 0 will remain the same
        ans = nums[0]
        for i in range(1, len(nums)):
            n = nums[i]
            ans = ans^n
        return ans
        
# @lc code=end

