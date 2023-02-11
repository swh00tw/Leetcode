#
# @lc app=leetcode id=1129 lang=python3
#
# [1129] Shortest Path with Alternating Colors
#

# @lc code=start
# inspired by sol: https://leetcode.com/problems/shortest-path-with-alternating-colors/solutions/3170218/python3-78-ms-faster-than-98-53-of-python3/
RED = 0
BLUE = 1

# input RED | BLUE
def toggleColor(color):
    return 1 - color

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # build graph as adjList
        graph = [[[], []] for i in range(n)] 
        # [[], []] is adjList for each node, the 0th slot is for red neighbors, the 1st slot is for blue neighbors
        for start, end in redEdges: 
            graph[start][RED].append(end)
        for start, end in blueEdges: 
            graph[start][BLUE].append(end)
        
        # init node 0 for BFS
        distances = [[0, 0]] + [[float("inf"), float("inf")] for i in range(n-1)] # [red SP, blue SP]
        q = [[0, RED], [0, BLUE]] # store [nodeIndex, seekingColor]
        while q:
            nodeIndex, seekingColor = q.pop(0)
            for neighborIndex in graph[nodeIndex][seekingColor]:
                if distances[neighborIndex][seekingColor] == float("inf"):
                    distances[neighborIndex][seekingColor] = distances[nodeIndex][toggleColor(seekingColor)]+1
                    q.append([neighborIndex, toggleColor(seekingColor)])
        res = []
        for i in range(n):
            minimum = min(distances[i][RED], distances[i][BLUE])
            res.append(-1 if minimum == float("inf") else minimum)
        return res
# @lc code=end

