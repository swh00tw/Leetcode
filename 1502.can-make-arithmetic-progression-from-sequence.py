#
# @lc app=leetcode id=1502 lang=python3
#
# [1502] Can Make Arithmetic Progression From Sequence
#

# @lc code=start
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        n = len(arr)
        maxNum = max(arr)
        minNum = min(arr)
        unit = (maxNum-minNum)/(n-1)
        nums = set(arr)
        for i in range(n):
            expected = minNum + i*unit
            if expected not in nums:
                return False
        return True

        # arr.sort()
        # diff = arr[1]-arr[0]
        # if len(arr)==2:
        #     return True
        # for i in range(2, len(arr)):
        #     if (arr[i]-arr[i-1]) != diff:
        #         return False
        # return True
        
# @lc code=end

