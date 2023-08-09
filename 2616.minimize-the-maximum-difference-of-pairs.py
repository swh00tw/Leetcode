#
# @lc app=leetcode id=2616 lang=python3
#
# [2616] Minimize the Maximum Difference of Pairs
#

# @lc code=start
import heapq


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        # binary search the answer
        # the answer must within certain range
        nums = list(sorted(nums))
        l, r = 0, nums[-1] - nums[0]  # the upper bound and lower bound of answer
        n = len(nums)
        while l <= r:
            # guess answer is mid
            mid = (l + r) // 2
            pairsCount = 0
            # if the number of pairs that their diff value below or equal mid is exactly p
            # we find the answer
            # if lower, the answer should be higher
            # else, lower
            idx = 0
            while idx < n - 1:
                if nums[idx + 1] - nums[idx] <= mid:
                    pairsCount += 1
                    idx += 2  # we need to skip next pair since cannot reuse same number
                else:
                    idx += 1
            # since there might be more than one answer that satisfy the requirement that having exactly p pairs value below mid
            # find the lowest one
            if pairsCount < p:
                l = mid + 1
            else:
                r = mid - 1
        return l


# @lc code=end
