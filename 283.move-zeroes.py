#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
# ref: https://leetcode.com/problems/move-zeroes/solutions/172432/the-easiest-but-unusual-snowball-java-solution-beats-100-o-n-clear-explanation/
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroSize = 0
        for i in range(len(nums)):
            if nums[i]==0:
                zeroSize+=1
            else:
                if zeroSize>0:
                    nums[i], nums[i-zeroSize] = 0, nums[i]

        # i = 0
        # n = len(nums)
        # while i<n:
        #     if nums[i]==0:
        #         j =i+1
        #         while j<n:
        #             if nums[j]!=0:
        #                 # swap
        #                 nums[i], nums[j] = nums[j], nums[i]
        #                 break
        #             j+=1
        #     i+=1

# @lc code=end

