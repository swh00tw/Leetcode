#
# @lc app=leetcode id=703 lang=python3
#
# [703] Kth Largest Element in a Stream
#

# @lc code=start
# ref: https://leetcode.com/problems/kth-largest-element-in-a-stream/solutions/3553820/python-java-c-simple-solution-easy-to-understand/
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        elif val > self.min_heap[0]:
            heapq.heapreplace(self.min_heap, val)
        return self.min_heap[0]
    
# my first sol:
# class KthLargest:

#     def __init__(self, k: int, nums: List[int]):
#         self.k = k
#         self.nums = sorted(nums)

#     def add(self, val: int) -> int:
#         # binary search to find where to add
#         l = 0
#         r = len(self.nums)-1
#         while l<=r:
#             mid = (l+r)//2
#             if self.nums[mid]>=val:
#                 r = mid-1
#             else:
#                 l = mid+1
#         self.nums = self.nums[:l]+[val]+self.nums[l:]
#         return self.nums[-self.k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end

