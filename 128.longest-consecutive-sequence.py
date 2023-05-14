#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
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
        if ri != rj:
            self.root[rj] = ri
    def getParents(self):
        return self.root

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # eliminate duplicate number
        newNums = []
        s = set()
        for n in nums:
            if n in s:
                continue
            else:
                s.add(n)
                newNums.append(n)
        # use union find
        # create a map from num of idx
        numIdxMap = {}
        for i, n in enumerate(newNums):
            numIdxMap[n] = i
        uf = UnionFind(len(newNums))
        for i, n in enumerate(newNums):
            if n-1 in numIdxMap:
                uf.union(i, numIdxMap[n-1])
            if n+1 in numIdxMap:
                uf.union(i, numIdxMap[n+1])
        # ??
        for n in range(len(newNums)):
            uf.find(n)
        parents = uf.getParents()
        # count freq of each parent and return the max freq
        d = {}
        for p in parents:
            if d.get(p):
                d[p]+=1
            else:
                d[p]=1
        return max(d.values())
        
# @lc code=end

