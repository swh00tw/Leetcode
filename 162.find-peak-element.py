#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l , r = 0, len(nums)-1
        n = len(nums)
        while l<=r:
            mid = (l+r)//2
            if nums[mid] > (nums[mid+1] if mid+1<n else -inf) and nums[mid] > (nums[mid-1] if mid-1>=0 else -inf):
                return mid
            elif nums[mid]<nums[mid+1] and mid+1<n:
                l = mid+1
            elif nums[mid]<nums[mid-1] and mid-1>=0:
                r = mid -1
        
        
# @lc code=end

