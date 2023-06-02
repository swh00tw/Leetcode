#
# @lc app=leetcode id=2101 lang=python3
#
# [2101] Detonate the Maximum Bombs
#

# @lc code=start
from collections import defaultdict
import math
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # reduce the problem to a graph problem
        # it can be represented by unidirected unweighted graph, if A node can induce B node, there's a edge from A to B
        # the answer is the node that can reach the maximum number of nodes
        # create a adjList first
        n = len(bombs)
        adjList = defaultdict(list)
        for srcIdx, src in enumerate(bombs):
            for dstIdx, dst in enumerate(bombs):
                if srcIdx!=dstIdx:
                    distance = math.pow(src[0]-dst[0],2)+math.pow(src[1]-dst[1],2)
                    if (src[2]**2)>=distance:
                        adjList[srcIdx].append(dstIdx)
        # run BFS for each node
        answer = -inf # the number of nodes that can reach
        for srcIdx in range(n):
            nodeCount = 0
            visited = [False]*n
            q = [srcIdx]
            visited[srcIdx]=True
            while q:
                nodeIdx = q.pop(0)
                nodeCount += 1
                for adjNodeIdx in adjList[nodeIdx]:
                    if visited[adjNodeIdx]==False:
                        q.append(adjNodeIdx)
                        visited[adjNodeIdx]=True
            if nodeCount>answer:
                answer = nodeCount
        return answer



        
# @lc code=end

