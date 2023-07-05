#
# @lc app=leetcode id=1493 lang=python3
#
# [1493] Longest Subarray of 1's After Deleting One Element
#


# @lc code=start
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # we got one chance to skip one zero
        # if we encounter zero and have no chance left
        # restore the chance to skip from the last time we used it
        # need to recalculate ones from the previous zero
        # so move start pointer and minus the unvalid one's
        best = 0
        count = 0
        chance = 1
        startIdx = 0
        for i, n in enumerate(nums):
            if n == 1:
                count += 1
                best = max(best, count)
            elif n == 0 and chance == 1:
                chance -= 1
                continue
            else:
                while nums[startIdx] != 0:
                    startIdx += 1
                    count -= 1
                startIdx += 1  # move to the right of the zero
        return best - 1 if chance == 1 else best


# @lc code=end
