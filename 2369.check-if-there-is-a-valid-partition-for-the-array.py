#
# @lc app=leetcode id=2369 lang=python3
#
# [2369] Check if There is a Valid Partition For The Array
#


# @lc code=start
class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        cache = {}
        n = len(nums)

        def solve(startIdx):
            # top down dp
            if startIdx in cache:
                return cache[startIdx]
            # base case
            if startIdx == n:
                return True
            if startIdx + 1 == n:
                return False
            elif n == startIdx + 2:
                return nums[startIdx] == nums[startIdx + 1]
            elif n == startIdx + 3:
                if nums[startIdx] == nums[startIdx + 1] == nums[startIdx + 2]:
                    return True
                return (
                    nums[startIdx] + 1 == nums[startIdx + 1]
                    and nums[startIdx + 1] + 1 == nums[startIdx + 2]
                )

            check1 = self.checkFirstRule(nums, startIdx)
            if check1:
                if solve(startIdx + 2):
                    cache[startIdx] = True
                    return True

            check2 = self.checkSecondRule(nums, startIdx)
            if check2:
                if solve(startIdx + 3):
                    cache[startIdx] = True
                    return True

            check3 = self.checkThirdRule(nums, startIdx)
            if check3:
                if solve(startIdx + 3):
                    cache[startIdx] = True
                    return True

            cache[startIdx] = False
            return False

        return solve(0)

    def checkFirstRule(self, nums, s):
        return nums[s] == nums[s + 1] and s + 2 < len(nums)

    def checkSecondRule(self, nums, s):
        return s + 3 < len(nums) and nums[s] == nums[s + 1] == nums[s + 2]

    def checkThirdRule(self, nums, s):
        return (
            len(nums) > s + 3
            and nums[s] + 1 == nums[s + 1]
            and nums[s + 1] + 1 == nums[s + 2]
        )


# @lc code=end
