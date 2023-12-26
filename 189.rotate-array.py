#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#


# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.sol3(nums, k)

    def sol1(self, nums, k):
        # SC: O(n)
        # TC: O(n)
        n = len(nums)
        res = [0] * n
        for i in range(n):
            target = (i + k) % n
            res[target] = nums[i]
        for i in range(n):
            nums[i] = res[i]

    def sol2(self, nums, k):
        # SC: O(n)
        # TC: O(n)
        # k is always lower than the length of array
        k = k % len(nums)
        # repeat nums two times
        arr = nums + nums
        n = len(nums)
        for i in range(n):
            nums[i] = arr[-k + i]


# @lc code=end
