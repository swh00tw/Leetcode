#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            d[n]=i
        for i in range(len(nums)):
            if target-nums[i] in d and (d[target-nums[i]])!=i:
                return [i,d[target-nums[i]]]
# @lc code=end

