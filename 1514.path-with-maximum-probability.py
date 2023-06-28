#
# @lc app=leetcode id=1514 lang=python3
#
# [1514] Path with Maximum Probability
#

# @lc code=start
import heapq
from collections import defaultdict
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        # dijkstra
        adjList = defaultdict(list)
        for i in range(len(succProb)):
            adjList[edges[i][0]].append((edges[i][1], succProb[i]))
            adjList[edges[i][1]].append((edges[i][0], succProb[i]))
        q = [(-1, start)] # maxHeap
        heapq.heapify(q)
        value = [-1]*n
        value[start] = 1
        while q:
            negativeNodeVal, nodeIdx = heapq.heappop(q) # get node w/ maxValue to avoid revisiting
            nodeVal = -negativeNodeVal
            if nodeIdx==end:
                return nodeVal
            for idx, prob in adjList[nodeIdx]:
                if nodeVal*prob > value[idx]:
                    value[idx] = nodeVal*prob
                    heapq.heappush(q, (-value[idx], idx))
        return 0

        
# @lc code=end

