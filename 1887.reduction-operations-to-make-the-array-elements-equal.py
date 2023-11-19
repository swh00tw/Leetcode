#
# @lc app=leetcode id=1887 lang=python3
#
# [1887] Reduction Operations to Make the Array Elements Equal
#


# @lc code=start
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        # sort nums first
        nums.sort()
        if nums[0] == nums[-1]:
            return 0
        ans = 0
        for i in range(1, len(nums)):
            prev = nums[i - 1]
            curr = nums[i]
            if prev != curr:
                ans += len(nums) - i
        return ans


# @lc code=end
