#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.binarySearchL(nums, target), self.binarySearchR(nums, target)]

    def binarySearchL(self, nums, target):
        l = 0
        r = len(nums)-1
        while l<=r:
            middle = (l+r)//2
            if nums[middle]>=target:
                r = middle - 1
            else:
                l = middle + 1
        return l if 0<= l <= len(nums)-1 and nums[l]==target else -1
    def binarySearchR(self, nums, target):
        l, r = 0, len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]>target:
                r = mid - 1
            else:
                l = mid + 1
        return r if  0<= r <= len(nums)-1 and nums[r]==target else -1

        
# @lc code=end

