#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        islands = 0
        unVisitedOnes = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j]=="1":
                    unVisitedOnes.add((i, j))
        def isUnvisitedOne(x, y):
            return grid[x][y]=="1" and (x, y) in unVisitedOnes
        while len(unVisitedOnes)>0:
            randomNode = unVisitedOnes.pop()
            islands+=1
            # bfs
            s = [randomNode]
            while s:
                x, y = s.pop(0)
                if y-1>=0 and isUnvisitedOne(x, y-1):
                    s.append((x, y-1))
                    unVisitedOnes.discard((x, y-1))
                if y+1<m and isUnvisitedOne(x, y+1):
                    s.append((x, y+1))
                    unVisitedOnes.discard((x, y+1))
                if x-1>=0 and isUnvisitedOne(x-1, y):
                    s.append((x-1, y))
                    unVisitedOnes.discard((x-1, y))
                if x+1<n and isUnvisitedOne(x+1, y):
                    s.append((x+1, y))
                    unVisitedOnes.discard((x+1, y))
        return islands
        
# @lc code=end

