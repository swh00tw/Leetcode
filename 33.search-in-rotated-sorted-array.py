#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#


# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # similar binary search as question 153
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if target > nums[mid]:
                if nums[r] < nums[mid]:
                    l = mid + 1
                else:
                    if nums[r] >= target:
                        l = mid + 1
                    else:
                        r = mid - 1
            else:
                if nums[l] > nums[mid]:
                    r = mid - 1
                else:
                    if nums[l] <= target:
                        r = mid - 1
                    else:
                        l = mid + 1
        return -1


# @lc code=end
