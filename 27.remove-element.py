#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#


# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # create a pointer point to the next index which should be filled
        # use a for loop to traverse the whole nums
        # if encounter num == val:
        #   currIdx remains unchanged, continue
        # else:
        #   fill the num to currIdx
        currIdx = 0
        n = len(nums)
        for i in range(n):
            num = nums[i]
            if num != val:
                nums[currIdx] = num
                currIdx += 1
        return currIdx


# @lc code=end
