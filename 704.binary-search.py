#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
from math import ceil
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(0, len(nums)-1, nums, target)

    def binarySearch(self, startIdx, endIdx, arr, target):
        if startIdx>endIdx:
            return -1
        middleIdx = ceil((startIdx + endIdx)/2)
        if target == arr[middleIdx]:
            return middleIdx
        elif target < arr[middleIdx]:
            return self.binarySearch(startIdx, middleIdx-1, arr, target)
        else:
            return self.binarySearch(middleIdx+1, endIdx, arr, target)
        
# @lc code=end

