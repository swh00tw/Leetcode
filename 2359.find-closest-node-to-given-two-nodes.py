#
# @lc app=leetcode id=2359 lang=python3
#
# [2359] Find Closest Node to Given Two Nodes
#

# @lc code=start
class Node:
    def __init__(self, id, adj=[]):
        self.id = id
        self.adj = adj

class Graph:
    def __init__(self, nodes):
        self.nodes = nodes

    def getNode(self, id):
        return self.nodes[id]

    def runSSSP(self, startIndex):
        # BFS
        distances = [float("inf")]*len(self.nodes)
        # init
        distances[startIndex] = 0
        queue=[startIndex]
        while queue:
            nodeIndex = queue.pop(0)
            node = self.getNode(nodeIndex)
            for adjIndex in node.adj:
                if distances[adjIndex]==float("inf"):
                    distances[adjIndex] = distances[nodeIndex]+1
                    queue.append(adjIndex)
        return distances



class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        # first, build a graph
        nodes = []
        for nodeIndex, adjIndex in enumerate(edges):
            adjNodes = [] if adjIndex == -1 else [adjIndex]
            nodes.append(Node(nodeIndex, adjNodes))
        graph = Graph(nodes)
        # run SSSP from node1 and node2
        distancesFromNode1 = graph.runSSSP(node1)
        distancesFromNode2 = graph.runSSSP(node2)
        # use the result from both to find the closest node
        minimum = float("inf")
        answerNodeIndex = -1
        for i in range(len(distancesFromNode1)):
            if distancesFromNode1[i]!=float("inf") and distancesFromNode2[i]!=float("inf"):
                maximum = max(distancesFromNode1[i],distancesFromNode2[i])
                if maximum < minimum:
                    # update minimum and answerNodeIndex
                    minimum = maximum
                    answerNodeIndex = i
        return answerNodeIndex

        
# @lc code=end

