#
# @lc app=leetcode id=1466 lang=python3
#
# [1466] Reorder Routes to Make All Paths Lead to the City Zero
#

# @lc code=start
from collections import defaultdict, deque


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # use a adj matrix to represent (directed) graph
        # from source node 0, run bfs or dfs to traverse the graph
        # if at node A, and between node A and node B have a link, find one reverse link, count it
        # return count
        oldRoads = set([(i, j) for i, j in connections])
        adjList = defaultdict(list)
        for src, dst in connections:
            adjList[src].append(dst)
            adjList[dst].append(src)
        # DFS
        visited = [False] * n
        visited[0] = True
        q = deque([0])
        newRoads = []
        while q:
            idx = q.popleft()
            for adjNodeIdx in adjList[idx]:
                if not visited[adjNodeIdx]:
                    newRoads.append((adjNodeIdx, idx))
                    q.append(adjNodeIdx)
                    visited[adjNodeIdx] = True

        ans = 0
        for src, dst in newRoads:
            if (src, dst) not in oldRoads:
                ans += 1
        return ans


# @lc code=end
