#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

from math import ceil
class Solution:
    def firstBadVersion(self, n: int) -> int:
        # binary search
        return self.binarySearch(1, n)

    def binarySearch(self, start, end):
        if start>end:
            return -1 # this case should never happen
        middle = ceil((start+end)/2)
        if isBadVersion(middle)==False:
            return self.binarySearch(middle+1, end)
        else:
            if isBadVersion(middle-1)==False:
                return middle
            else:
                return self.binarySearch(start, middle-1)

        
        
# @lc code=end

