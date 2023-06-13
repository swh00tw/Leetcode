#
# @lc app=leetcode id=1466 lang=python3
#
# [1466] Reorder Routes to Make All Paths Lead to the City Zero
#

# @lc code=start
from collections import defaultdict
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # create a undirected graph
        # use BFS to visit all nodes from 0
        # if the edges we use is in the opposite direction than expected, increment count by 1
        adjList = defaultdict(list)
        reverseRoutes = set()
        for src, dst in connections:
            adjList[src].append(dst)
            adjList[dst].append(src)
            reverseRoutes.add((dst, src))
        # BFS
        count = 0
        visited = [False]*n
        visited[0]=True
        q = [0]
        while q:
            cityIdx = q.pop(0)
            for adjIdx in adjList[cityIdx]:
                if visited[adjIdx]==False:
                    visited[adjIdx]=True
                    q.append(adjIdx)
                    if (cityIdx, adjIdx) not in reverseRoutes:
                        count+=1
        return count
# @lc code=end

