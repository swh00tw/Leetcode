#
# @lc app=leetcode id=2336 lang=python3
#
# [2336] Smallest Number in Infinite Set
#

# @lc code=start
import heapq
class SmallestInfiniteSet:

    def __init__(self):
        self.minNum = 1 # keep track of current starting number of continuous part
        self.pq = [] # priority queue (minHeap) store the numbers added back (smaller than minNum ofc)

    def popSmallest(self) -> int:
        if len(self.pq)!=0:
            return heapq.heappop(self.pq)
        else:
            self.minNum+=1
            return self.minNum-1

    def addBack(self, num: int) -> None:
        if num< self.minNum and num not in self.pq:
            heapq.heappush(self.pq, num)

        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
# @lc code=end

