#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#


# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            bitSum = 0
            for n in nums:
                # if n is negative, toggle the unused 31st bit to 1
                # if n is positive, the 31st bit will always be 0 since the max positive number is 2**31-1
                if n < 0:
                    n = n & (2**32 - 1)
                bitSum += (n >> i) & 1
            if bitSum % 3 == 1:
                ans |= 1 << i
        # if 31st bit is 1, the answer if negative, convert back and return
        if (ans >> 31) & 1:
            ans -= 2**32
        return ans


# @lc code=end
