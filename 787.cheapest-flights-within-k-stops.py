#
# @lc app=leetcode id=787 lang=python3
#
# [787] Cheapest Flights Within K Stops
#

# @lc code=start
class Edge:
    def __init__(self, src: int, dst: int, weight: int):
        self.src = src
        self.dst = dst
        self.weight=weight
    def __repr__(self):
        return f"Edge src: {self.src}, dst: {self.dst}, w: {self.weight}"

class Node:
    def __init__(self, id: int, edges: List[Edge]=[]):
        self.id = id
        self.edges = edges
    def addEdge(self,edge):
        self.edges = self.edges + [edge]
    def __repr__(self):
        return f"Node {self.id}"

class Graph:
    def __init__(self, nodes: List[Node]):
        self.nodes = nodes
        self.n = len(nodes)
    def getNodeById(self, id):
        return self.nodes[id]
    def runSSSP(self, src, dst, maxStops):
        minPrices = [float("inf")]*self.n
        # modified from BFS
        queue = [(src, 0)] # node and minPriceWhenFirstDiscovered pair
        # KEY: note that we must store "minPriceWhenFirstDiscovered" in the queue
        # since minPrices[idx] might be updated through relaxations by node at the same level (same # of stop from src)
        # and that's not what we want (it will cause shortestPath and cheapestPath point to different routes)
        stops = 0
        # each while iteration means we move one stop forward from current DISCOVERED nodes
        while queue and stops<=maxStops:
            size = len(queue)
            # iterate through all "DISCOVERED" nodes and do relaxation for all edges of these nodes
            for i in range(size):
                nodeIdx, minPrice = queue.pop(0)
                node = self.getNodeById(nodeIdx)
                # do relaxation for each adjacent nodes
                for edge in node.edges:
                    dstIdx = edge.dst
                    if edge.weight + minPrice < minPrices[dstIdx]:
                        minPrices[dstIdx]=edge.weight + minPrice
                        queue.append((dstIdx, minPrices[dstIdx])) # append newly discovered node idx and minPriceWhenFirstDiscovered 
            stops+=1       
        return -1 if minPrices[dst]==float("inf") else minPrices[dst]


# ref: https://leetcode.com/problems/cheapest-flights-within-k-stops/solutions/3099885/day-26-simple-bfs-easiest-beginner-friendly-solution/
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # init
        nodes=[]
        for i in range(n):
            nodes.append(Node(i))
        for e in flights:
            srcIdx=e[0]
            dstIdx=e[1]
            weight=e[2]
            edge=Edge(srcIdx,dstIdx,weight)
            nodes[srcIdx].addEdge(edge)
        # checkpoint
        # for n in nodes:
        #     print("Node", n.id)
        #     for e in n.edges:
        #         print(e)
        graph = Graph(nodes)
        # run algorithm
        res = graph.runSSSP(src, dst, k)
        return res


        
# @lc code=end

