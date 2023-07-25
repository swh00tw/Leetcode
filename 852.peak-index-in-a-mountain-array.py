#
# @lc app=leetcode id=852 lang=python3
#
# [852] Peak Index in a Mountain Array
#


# @lc code=start
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        l, r = 1, n - 2
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return mid
            if arr[mid] < arr[mid + 1]:
                l = mid + 1
            else:
                r = mid - 1


# @lc code=end
