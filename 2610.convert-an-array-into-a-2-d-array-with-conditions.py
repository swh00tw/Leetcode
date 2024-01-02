#
# @lc app=leetcode id=2610 lang=python3
#
# [2610] Convert an Array Into a 2D Array With Conditions
#

# @lc code=start
from collections import Counter


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        # count the freq of each number
        # the number of rows is max value in the Counter
        # distribute the same number into different row
        freq = Counter(nums)
        rows = max(freq.values())
        mat = [[] for _ in range(rows)]
        for n in nums:
            # determine which row
            # see freq
            if freq[n] > 0:
                rowIdx = freq[n] - 1
                mat[rowIdx].append(n)
                freq[n] -= 1
        return mat


# @lc code=end
