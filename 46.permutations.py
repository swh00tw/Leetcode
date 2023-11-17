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
            # remove
            nums.pop(i)
            # compute
            for sub_ans in self.permute(nums):
                ans.append([n] + sub_ans)
            # recover
            nums.insert(i, n)
        return ans


# @lc code=end
