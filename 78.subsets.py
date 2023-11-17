#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#


# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # use subsets function as recursive function
        # pop the first element of nums --> number X
        # call subset again to retrieve all possible subsets Y of nums[1:]
        # return all possible subsets which can be formed by using number X and subsets Y
        # X can decide whether join these subset or not, so the answer can be derived from two source
        # 1. X + Y     --> X join subsets of Y
        # 2. Y itself  --> X did not join
        n = len(nums)
        # base case
        if n == 1:
            return [nums, []]

        x = nums[0]
        y = self.subsets(nums[1:])
        res = y + [[x] + s for s in y]
        return res


# @lc code=end
