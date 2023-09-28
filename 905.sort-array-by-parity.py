#
# @lc app=leetcode id=905 lang=python3
#
# [905] Sort Array By Parity
#


# @lc code=start
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # two pointers
        # l, r = 0, len(nums)-1
        # l search for odd
        # r search for even
        # keep swapping the number left pointer find and the number right pointer find
        n = len(nums)
        if n == 1:
            return nums

        l, r = 0, n - 1
        while l <= r:
            while l < n and nums[l] % 2 == 0:
                l += 1
            while r >= 0 and nums[r] % 2 == 1:
                r -= 1
            if l == n or r < 0 or l > r:
                break
            # swap
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        return nums


# @lc code=end
