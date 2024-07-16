#
# @lc app=leetcode id=547 lang=python3
#
# [547] Number of Provinces
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
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry:
            if self.rank[rx] < self.rank[ry]:
                self.root[rx] = ry
            elif self.rank[ry] < self.root[rx]:
                self.root[ry] = rx
            else:
                self.root[rx] = ry
                self.rank[ry] += 1

    def getNumProvinces(self):
        n = len(self.root)
        for i in range(n):
            self.find(i)
        rootSet = set(self.root)
        return len(rootSet)


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)
        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j] == 1:
                    uf.union(i, j)
        return uf.getNumProvinces()


# @lc code=end
