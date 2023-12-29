#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#


# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # sliding window
        # keep moving right pointer
        # if the sum is larger than target
        # try to shrink by moving left pointer
        startIdx = 0
        acc = 0
        res = float("inf")
        for endIdx in range(len(nums)):
            acc += nums[endIdx]
            while acc >= target and startIdx <= endIdx:
                # update res
                res = min(res, endIdx + 1 - startIdx)
                # shrink
                acc -= nums[startIdx]
                startIdx += 1
        return res if res < float("inf") else 0


# @lc code=end
