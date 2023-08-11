#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#


# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search
        # only two senario of mid point
        # if nums[mid-1]>nums[mid] && nums[mid+1]>nums[mid], return ans
        # else:
        #   if nums[r]<nums[mid], the answer must in upper half
        #   else: lower half
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if (nums[mid - 1] > nums[mid] if mid - 1 >= 0 else True) and (
                nums[mid + 1] > nums[mid] if mid + 1 < len(nums) else True
            ):
                return nums[mid]
            else:
                if nums[r] < nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1


# @lc code=end
