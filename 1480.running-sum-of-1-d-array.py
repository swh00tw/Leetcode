#
# @lc app=leetcode id=1480 lang=python3
#
# [1480] Running Sum of 1d Array
#

# @lc code=start
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        currSum = 0
        for i in range(len(nums)):
            newNum = nums[i]
            currSum += newNum
            res.append(currSum)
        return res
# @lc code=end

