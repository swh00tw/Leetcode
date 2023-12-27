#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#


# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointers
        l, r = 0, len(numbers) - 1
        while l < r:
            n1 = numbers[l]
            n2 = numbers[r]
            n = n1 + n2
            if target == n:
                return [l + 1, r + 1]
            elif target < n:
                r -= 1
            else:
                l += 1


# @lc code=end
