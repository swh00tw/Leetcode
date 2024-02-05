#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#

# @lc code=start
from collections import defaultdict


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        # build the graph using equation,
        # build adjList, store (neighbor, weight)
        self.adjList = defaultdict(list)
        for i, pair in enumerate(equations):
            weight = values[i]
            src, dst = pair
            self.adjList[src].append((dst, weight))
            self.adjList[dst].append((src, 1 / weight))
        return [self.getAns(src, dst) for src, dst in queries]

    def getAns(self, src, dst):
        if src not in self.adjList or dst not in self.adjList:
            return -1.0
        if src == dst:
            return 1.0
        # run DFS + backtracking to get answer
        # backtracking: remove this node before entering deeper recursion to avoid duplicate
        # remember to add back before any return to make sure the graph will be remain the same after each call
        key, arr = src, self.adjList[src]
        del self.adjList[src]
        for neighbor, weight in arr:
            ans = weight * self.getAns(neighbor, dst)
            if ans >= 0:
                self.adjList[key] = arr
                return ans
        self.adjList[key] = arr
        return -1.0


# @lc code=end
