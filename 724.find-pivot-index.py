#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#


# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # calculate running sum, sums[i] = nums[0] + ... + nums[i]
        curr = 0
        sums = []
        for n in nums:
            curr += n
            sums.append(curr)
        # find pivot index
        for i, n in enumerate(nums):
            left_sum = 0 if i == 0 else sums[i - 1]
            right_sum = 0 if i == len(nums) - 1 else (sums[-1] - sums[i])
            if left_sum == right_sum:
                return i
        return -1


# @lc code=end
