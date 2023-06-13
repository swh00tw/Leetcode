#
# @lc app=leetcode id=547 lang=python3
#
# [547] Number of Provinces
#

# @lc code=start
class UnionFind:
    def __init__(self, n):
        self.root = list(range(n))
        self.rank = [0]*n
    def find(self, n):
        if self.root[n]!=n:
            self.root[n] = self.find(self.root[n])
        return self.root[n]
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx!=ry:
            if self.rank[rx]>self.rank[ry]:
                self.root[ry] = rx
            elif self.rank[ry]>self.rank[rx]:
                self.root[rx] = ry
            else:
                self.root[rx] = ry
                self.rank[ry] += 1
    def getDisjointSets(self):
        res = set()
        for i in range(len(self.root)):
            res.add(self.find(i))
        return res
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)
        for i in range(n):
            for j in range(i, n):
                if i!=j and isConnected[i][j]==1:
                    uf.union(i, j)
        return len(uf.getDisjointSets())

# @lc code=end

