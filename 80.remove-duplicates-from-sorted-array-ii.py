#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#


# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # maintain a pointer points to next index which should be written
        # traverse the nums array, whenever encounter a new number, start counting,
        # if counting >=2, continue
        count = 0
        next_idx = 0
        for i, num in enumerate(nums):
            # new start
            if i == 0 or nums[i - 1] != nums[i]:
                count = 0
            if count < 2:
                nums[next_idx] = num
                next_idx += 1
                count += 1
        return next_idx


# @lc code=end
