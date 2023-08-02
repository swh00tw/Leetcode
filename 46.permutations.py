#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#


# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        ans = []
        for i, n in enumerate(nums):
            tmp = nums[:]
            del tmp[i]
            for subans in self.permute(tmp):
                ans.append(subans + [n])
        return ans


# @lc code=end
