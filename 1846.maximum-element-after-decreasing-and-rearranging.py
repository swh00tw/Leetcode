#
# @lc app=leetcode id=1846 lang=python3
#
# [1846] Maximum Element After Decreasing and Rearranging
#

# @lc code=start
from collections import Counter


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        # sort the arr
        # map the first number to 1
        # the second number to 2
        # ...
        # arr: [2, 2, 2, 7, 8, 9]
        # mapped: [1, 2, 3, 4, 5, 6]

        # during the convertion, mind the upper bound
        # if the mapped[i] is larger than arr[i], use previous old number mapped[i-1]
        arr = list(sorted(arr))
        curr = 1
        for i in range(len(arr)):
            new_val = 1 if i == 0 else curr + 1
            if new_val > arr[i]:
                curr = arr[i]
            else:
                curr = new_val
        return curr


# @lc code=end
