#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#


# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums = sorted(nums)
        n = len(nums)
        for i, num in enumerate(nums[:-2]):
            numSet = set()
            target = (-1) * num
            for j in range(i + 1, n):
                val = nums[j]
                if target - val in numSet:
                    ans.add((num, min(target - val, val), max(target - val, val)))
                numSet.add(val)
        return [list(triplet) for triplet in ans]


# @lc code=end
