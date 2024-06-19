#
# @lc app=leetcode id=1493 lang=python3
#
# [1493] Longest Subarray of 1's After Deleting One Element
#


# @lc code=start
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # have one chance to skip a zero
        # sliding window
        # left pointer always point to the left of the window
        # if have no chance and encounter next zero
        # move left pointer to the right of the zero (recycle the power of skipping zero)
        best = 0
        n = len(nums)
        left = 0
        chance = 1
        for right in range(n):
            num = nums[right]
            if num == 0:
                if chance == 1:
                    chance = 0
                else:
                    # recycle
                    while left <= right:
                        if nums[left] == 0:
                            break
                        left += 1
                    left += 1
            best = max(best, right + 1 - left - (1 if chance == 0 else 0))

        # must delete an element even if no zero
        if chance == 1:
            return best - 1
        return best


# @lc code=end
