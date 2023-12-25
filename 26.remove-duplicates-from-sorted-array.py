#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#


# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # create a pointer point to next idx which should be filled
        # iterate thru whole nums array, if current number is seen, ignore
        # else, mark it as seen and fill in the nextIdx position in nums, increment nextIdx
        nextIdx = 0
        seen = set()
        for _, num in enumerate(nums):
            if num in seen:
                continue
            nums[nextIdx] = num
            seen.add(num)
            nextIdx += 1
        return nextIdx


# @lc code=end
