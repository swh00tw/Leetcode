#
# @lc app=leetcode id=1464 lang=python3
#
# [1464] Maximum Product of Two Elements in an Array
#


# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max, second_max = 0, 0
        for num in nums:
            if num > max:
                second_max = max
                max = num
            elif num > second_max:
                second_max = num
        return (max - 1) * (second_max - 1)


# @lc code=end
