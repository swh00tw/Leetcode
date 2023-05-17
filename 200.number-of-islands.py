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
        visitedOnes = set()
        def isUnvisitedOne(x, y):
            return grid[x][y]=="1" and (x, y) not in visitedOnes
        for i in range(n):
            for j in range(m):
                if isUnvisitedOne(i, j):
                    # bfs
                    islands += 1
                    s = [(i, j)]
                    visitedOnes.add((i, j))
                    while s:
                        x, y = s.pop(0)
                        # append adjacent nodes in stack if there have value equal to "1"
                        if y-1>=0 and isUnvisitedOne(x, y-1):
                            s.append((x, y-1))
                            visitedOnes.add((x, y-1))
                        if y+1<m and isUnvisitedOne(x, y+1):
                            s.append((x, y+1))
                            visitedOnes.add((x, y+1))
                        if x-1>=0 and isUnvisitedOne(x-1, y):
                            s.append((x-1, y))
                            visitedOnes.add((x-1, y))
                        if x+1<n and isUnvisitedOne(x+1, y):
                            s.append((x+1, y))
                            visitedOnes.add((x+1, y))
        return islands
        
# @lc code=end

