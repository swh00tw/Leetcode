#
# @lc app=leetcode id=1579 lang=python3
#
# [1579] Remove Max Number of Edges to Keep Graph Fully Traversable
#

# @lc code=start
# ref: https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/solutions/3468004/python-java-c-simple-solution-easy-to-understand/
class UnionFind:
    def __init__(self, n):
        self.root = list(range(n+1))

    def find(self, i):
        # recursively find root
        if i != self.root[i]:
            self.root[i] = self.find(self.root[i])
        return self.root[i]

    def union(self, i, j): # return operation successful or not
        ri, rj = self.find(i), self.find(j)
        if ri == rj:
            return False
        else:
            self.root[rj] = ri
            return True

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # maintain two unionfind data structures for alice and bob respectively
        # first iterate through all type-3 edges
        aliceUf = UnionFind(n)
        bobUf = UnionFind(n)

        redundantEdges = 0
        aliceMSTEdges, bobMSTEdges = 0, 0

        # traverse type 3 first
        for t, i, j in edges:
            if t == 3:
                if aliceUf.union(i, j) and bobUf.union(i, j): #two data structures are identical now, they will only return (true, true) or (false, false)
                    aliceMSTEdges+=1
                    bobMSTEdges+=1
                else:
                    redundantEdges +=1
           
        # type 1 & 2
        for t, i, j in edges:
            if t==1:
                if aliceUf.union(i, j):
                    aliceMSTEdges+=1
                else:
                    redundantEdges+=1
            elif t==2:
                if bobUf.union(i, j):
                    bobMSTEdges+=1
                else:
                    redundantEdges+=1
            

        return redundantEdges if bobMSTEdges == n-1 == aliceMSTEdges else -1
        



# @lc code=end

