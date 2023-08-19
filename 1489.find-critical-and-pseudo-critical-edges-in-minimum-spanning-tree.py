#
# @lc app=leetcode id=1489 lang=python3
#
# [1489] Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree
#


# @lc code=start
class UnionFind:
    def __init__(self, n):
        self.root = list(range(n))
        self.rank = [0] * n

    def find(self, n):
        if self.root[n] != n:
            self.root[n] = self.find(self.root[n])
        return self.root[n]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            if self.rank[rx] < self.rank[ry]:
                self.root[rx] = ry
            elif self.rank[ry] < self.rank[rx]:
                self.root[ry] = rx
            else:
                self.root[rx] = ry
                self.rank[ry] += 1


class MSTBuilder:
    def __init__(self, n, edges, defaultEdgeIdx=None, excludeEdgeIdx=None):
        self.n = n
        self.edges = edges
        self.defaultEdgeIdx = defaultEdgeIdx
        self.excludeEdgeIdx = excludeEdgeIdx

    def getMSTWeight(self):
        uf = UnionFind(self.n)
        weight = 0

        if self.defaultEdgeIdx is not None:
            defaultEdge = self.edges[self.defaultEdgeIdx]
            weight += defaultEdge[2]
            uf.union(defaultEdge[0], defaultEdge[1])

        for i, e in enumerate(self.edges):
            if i == self.excludeEdgeIdx:
                continue
            if uf.find(e[0]) != uf.find(e[1]):
                uf.union(e[0], e[1])
                weight += e[2]

        # check if the edges form a MST, if not return inf
        for i in range(self.n):
            if uf.find(i) != uf.find(0):
                return inf

        return weight


class Solution:
    def findCriticalAndPseudoCriticalEdges(
        self, n: int, edges: List[List[int]]
    ) -> List[List[int]]:
        # sol: https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/solutions/3929059/beats-100-js-ts-java-c-c-python-python3-kotlin/
        critical, pseudoCritical = [], []
        # original index
        for i in range(len(edges)):
            edges[i].append(i)
        edges.sort(key=lambda x: x[2])
        mstWeight = MSTBuilder(n, edges).getMSTWeight()

        for i in range(len(edges)):
            e = edges[i]
            # try to remove the edge, if the weight increase, it's critical
            if mstWeight < MSTBuilder(n, edges, excludeEdgeIdx=i).getMSTWeight():
                critical.append(e[3])
            # if it's not critical, if using the edge we can get a MST, it's pseudo-critical
            elif mstWeight == MSTBuilder(n, edges, defaultEdgeIdx=i).getMSTWeight():
                pseudoCritical.append(e[3])

        return [critical, pseudoCritical]


# @lc code=end
