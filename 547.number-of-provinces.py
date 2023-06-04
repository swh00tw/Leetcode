#
# @lc app=leetcode id=547 lang=python3
#
# [547] Number of Provinces
#

# @lc code=start
class UnionFind:
    def __init__(self, n):
        self.root = list(range(n))
        self.degree = [0]*n 
    def find(self, n):
        # path compression
        if self.root[n]!=n: # it's not root
            self.root[n] = self.find(self.root[n])
        return self.root[n]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx!=ry:
            if self.degree[rx]<self.degree[ry]:
                self.root[rx] = ry
            elif self.degree[ry]<self.degree[rx]:
                self.root[ry] = rx
            else:
                self.root[rx] = ry
                self.degree[ry]+=1

    def getDisjoinSets(self):
        return set([self.find(i) for i in range(len(self.root))])

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # find SCCs
        # use Disjoint set (Union-find)
        n = len(isConnected)
        uf = UnionFind(n)
        # traverse all edges
        for i in range(n):
            for j in range(i+1, n):
                if i!=j and isConnected[i][j]==1:
                    uf.union(i, j)
        return len(uf.getDisjoinSets())
# @lc code=end

