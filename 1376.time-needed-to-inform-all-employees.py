#
# @lc app=leetcode id=1376 lang=python3
#
# [1376] Time Needed to Inform All Employees
#

# @lc code=start
from collections import defaultdict
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # BFS on directde, weighted graph
        adjList = defaultdict(list)
        for i, m in enumerate(manager):
            if m!=-1:
                adjList[m].append(i)
        # bfs
        farest = -1
        distance = [inf]*n
        q = [headID]
        distance[headID] = 0
        while q:
            nodeIdx = q.pop(0)
            farest = max(farest, distance[nodeIdx])
            for subordinateIdx in adjList[nodeIdx]:
                if distance[subordinateIdx]==inf:
                    q.append(subordinateIdx)
                    distance[subordinateIdx]=distance[nodeIdx]+informTime[nodeIdx]
        return farest
# @lc code=end

