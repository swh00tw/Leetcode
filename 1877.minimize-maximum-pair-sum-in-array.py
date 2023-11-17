#
# @lc app=leetcode id=1877 lang=python3
#
# [1877] Minimize Maximum Pair Sum in Array
#


# @lc code=start
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        # sort the array first
        # pair the i-th elemength with n-i-1, n is the length of the nums
        # compute pair sum
        ans = float("-inf")
        sorted_nums = list(sorted(nums))
        n = len(nums)
        for i in range(n // 2):
            ans = max(ans, sum([sorted_nums[i], sorted_nums[n - 1 - i]]))
        return ans


# @lc code=end
