#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # use max heap
        nums = [-n for n in nums]
        heapq.heapify(nums)
        ans = 0
        for _ in range(k):
            ans = -1 * heapq.heappop(nums)
        return ans


# @lc code=end
