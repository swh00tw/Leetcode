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
        # heapify the array
        # keep extract min k times
        count = 1
        ans = 0
        maxHeap = [-x for x in nums]
        heapq.heapify(maxHeap)
        while count <= k:
            ans = heapq.heappop(maxHeap)
            count += 1
        return -ans


# @lc code=end
