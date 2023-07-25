#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#


# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n - 1):
            # use binary search
            key = target - numbers[i]
            l, r = i + 1, n - 1
            while l <= r:
                mid = (l + r) // 2
                if numbers[mid] == key:
                    return [i + 1, mid + 1]
                else:
                    if numbers[mid] > key:
                        r = mid - 1
                    else:
                        l = mid + 1


# @lc code=end
