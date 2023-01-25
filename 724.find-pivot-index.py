#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#

# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        # apply running sum first
        runningSums = []
        currSum = 0
        for num in nums:
            currSum+=num
            runningSums.append(currSum)
        for i, runningSum in enumerate(runningSums):
            leftSum = 0 if i==0 else runningSums[i-1]
            rightSum = 0 if i == n-1 else runningSums[-1]-runningSum
            if leftSum == rightSum:
                return i
        return -1
        
# @lc code=end

