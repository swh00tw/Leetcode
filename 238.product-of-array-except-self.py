#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
from itertools import accumulate
import operator
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # pre[i]: prefix prod <= i
        # suf[i]: suffix prod >= i
        pre = list(accumulate(nums,operator.mul))
        suf = list(accumulate(nums[::-1], operator.mul))[::-1]

        res = []
        for i in range(len(nums)):
            if i==0:
                res.append(suf[i+1])
            elif i==len(nums)-1:
                res.append(pre[i-1])
            else:
                res.append(suf[i+1]*pre[i-1])
        return res

# @lc code=end

