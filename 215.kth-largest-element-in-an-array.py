#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # maintain a minHeap of size k
        # iterate through the array nums, in the end, the answer is root of the min heap
        # if the size bigger than k after push, remove the minimum and maintain heap variant
        heap=[]
        for i in nums:
            heapq.heappush(heap,i)       
            if len(heap)>k:        
                heapq.heappop(heap) 
                
        return heapq.heappop(heap)

                
# @lc code=end

