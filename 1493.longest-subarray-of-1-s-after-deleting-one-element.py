#
# @lc app=leetcode id=1493 lang=python3
#
# [1493] Longest Subarray of 1's After Deleting One Element
#


# @lc code=start
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # we got one chance to skip one zero
        # keep track of prev seen zero's index and the start counting index
        # if we encounter zero except for the first zero, update startCountingIdx and prevZeroIdx
        # if every step, count the length of the window between current idx and startCountingIdx
        best = 0
        chance = 1
        prevZeroIdx = 0
        startCountingIdx = 0
        for i, n in enumerate(nums):
            if n == 0 and chance == 1:
                chance -= 1
                prevZeroIdx = i
            elif n == 0 and chance == 0:
                startCountingIdx = prevZeroIdx + 1
                prevZeroIdx = i
            best = max(best, i - startCountingIdx)
        return best


# @lc code=end
