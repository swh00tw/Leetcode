#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#

# @lc code=start
from collections import defaultdict, deque


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        # build directed graph based on the equations
        # ["a", "b"], 3
        # "a" -> "b", 3 (a/b = 3)
        # "b" -> "a", 1/3 (b/a = 1/3)
        # adjList to repr graph
        # dfs or bfs to find answer for each query
        # ["a", "c"], start from "a" and see if can reach "c" and calculate the answer by weights
        # if not reachable, return -1.0
        adjList = defaultdict(list)
        n = len(values)
        for i in range(n):
            src, dst = equations[i]
            w = values[i]
            adjList[src].append((dst, w))
            adjList[dst].append((src, 1 / w))
        return [self.getAns(x, y, adjList) for x, y in queries]

    def getAns(self, a, b, adjList):
        # dfs
        if a not in adjList or b not in adjList:
            return -1.0
        if a == b:
            return 1
        k, v = a, adjList[a]
        del adjList[a]
        for neighbor, w in v:
            ans = w * self.getAns(neighbor, b, adjList)
            if ans <= 0:
                continue
            adjList[k] = v
            return ans
        adjList[k] = v
        return -1.0


# @lc code=end
