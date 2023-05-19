#
# @lc app=leetcode id=785 lang=python3
#
# [785] Is Graph Bipartite?
#

# @lc code=start
class UnionFind:
    def __init__(self, n):
        self.root = list(range(n))
        self.rank = [0]*n # union by rank optimization
    def find(self, n): #O(1)
        if self.root[n]!=n: # path compression (recursively update all parent's root val)
            self.root[n] = self.find(self.root[n])
        return self.root[n]
    def union(self, x, y): #O(1)
        rx, ry = self.find(x), self.find(y)
        if rx!=ry:
            if self.rank[rx]<self.rank[ry]:
                self.root[rx] = ry
            elif self.rank[rx]>self.rank[ry]:
                self.root[ry]=rx
            else:
                self.root[rx]=ry
                self.rank[ry]+=1
    def getSets(self):
        d = {}
        for nodeIdx, root in enumerate(self.root):
            if d.get(root):
                d[root].append(nodeIdx)
            else:
                d[root] = [nodeIdx]
        return d

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # use disjoint set to find all SCCs
        # apply bipartite check on each SCC
        # bipartite check: run a BFS, if find a colored neighbor with different color
        # white: undiscovered / blue, red: discovered
        n = len(graph)
        uf = UnionFind(n)
        for i in range(n):
            src = i
            for dst in graph[i]:
                uf.union(src, dst)
        res = []
        sets = uf.getSets()
        for root in sets:
            nodes = sets[root]
            res.append(self.isSetBipartite(graph, nodes[0]))
        print(res)
        return all(x == True for x in res)

    def isSetBipartite(self, graph, startIdx):
        BLUE = "blue"
        RED = "red"
        WHITE = "white"
        def getColor(s):
            return BLUE if s==RED else (RED if s==BLUE else WHITE)
        # bfs
        color = [WHITE]*len(graph)

        s = [startIdx]
        color[startIdx] = BLUE
        while s:
            nodeIdx = s.pop(0)
            for adjNode in graph[nodeIdx]:
                if color[adjNode]==WHITE:
                    color[adjNode]=getColor(color[nodeIdx])
                    s.append(adjNode)
                else:
                    # check if the same color, then return False
                    if color[adjNode]==color[nodeIdx]:
                        return False
        return True

# shorter sol: 
# no need to use disjoint set
# just iterate through all node
# if node is colored: continue
# else apply BFS, using my function above to check if it's bipartite

# @lc code=end

