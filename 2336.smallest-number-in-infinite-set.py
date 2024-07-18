#
# @lc app=leetcode id=2336 lang=python3
#
# [2336] Smallest Number in Infinite Set
#

# @lc code=start
import heapq


class SmallestInfiniteSet:

    def __init__(self):
        self.nextSmallestNum = 1
        self.pq = []  # store num put back
        self.numsPutback = set()

    def popSmallest(self) -> int:
        if not self.pq:
            ans = self.nextSmallestNum
            self.nextSmallestNum += 1
            return ans
        ans = heapq.heappop(self.pq)
        self.numsPutback.remove(ans)
        return ans

    def addBack(self, num: int) -> None:
        if num >= self.nextSmallestNum:
            return
        if num not in self.numsPutback:
            self.numsPutback.add(num)
            heapq.heappush(self.pq, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
# @lc code=end
