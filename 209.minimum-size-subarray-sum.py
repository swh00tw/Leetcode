#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#


# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 2 pointers
        # if the sum in window is less than sum, move right pointer
        # else, move left pointer
        l, r = 0, 0
        n = len(nums)
        currSum = nums[0]
        minLength = inf
        while l <= r:
            if currSum < target:
                r += 1
                if r == n:
                    break
                currSum += nums[r]
            else:
                minLength = min(minLength, r + 1 - l)
                currSum -= nums[l]
                l += 1
        return minLength if minLength < inf else 0


# @lc code=end
