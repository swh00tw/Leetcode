#
# @lc app=leetcode id=2462 lang=python3
#
# [2462] Total Cost to Hire K Workers
#

# @lc code=start
import heapq
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        totalCost = 0
        headPQ = costs[:candidates]
        tailPQ  = costs[max(candidates, len(costs)-candidates):]
        heapq.heapify(headPQ)
        heapq.heapify(tailPQ)
        # two pointers point to next number which is prepared to add into heap
        nextHead, nextTail = candidates, len(costs)-candidates-1
        for _ in range(k):
            if (not tailPQ and headPQ) or (tailPQ and headPQ and headPQ[0] <= tailPQ[0]):
                totalCost+=heapq.heappop(headPQ)
                if nextHead<=nextTail:
                    heapq.heappush(headPQ, costs[nextHead])
                    nextHead+=1
            elif (not headPQ and tailPQ) or (headPQ and tailPQ and tailPQ[0]<headPQ[0]):
                totalCost+=heapq.heappop(tailPQ)
                if nextHead<=nextTail:
                    heapq.heappush(tailPQ, costs[nextTail])
                    nextTail-=1
        return totalCost




        
# @lc code=end

