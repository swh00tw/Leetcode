#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#


# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # tortoise-hare algorithm
        # val is next index
        # find the start of the cycle
        # the prev node's val is the duplicate
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # run at same speed
        slow = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            if slow == fast:
                return slow


# @lc code=end
