#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#


# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # tortoise-hare algorithm
        slow, fast = nums[0], nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break

        fast = nums[0]
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]
        return fast


# @lc code=end
