#
# @lc app=leetcode id=1091 lang=python3
#
# [1091] Shortest Path in Binary Matrix
#

# @lc code=start
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        # bfs
        distance = [[inf]*n for _ in range(n)]
        q = [(0, 0)]
        distance[0][0] = 1

        def visitCell(x, y, d): 
            # visitNeighbor, if its unvisited, enqueue
            if distance[x][y]==inf:
                q.append((x, y))
            # relax everytime
            distance[x][y] = min(distance[x][y], d)
        while q:
            x, y = q.pop(0)
            newD = distance[x][y]+1
            # top
            if x-1>=0:
                if grid[x-1][y]==0:
                    visitCell(x-1, y, newD)
                # top left
                if y-1>=0 and grid[x-1][y-1]==0:
                    visitCell(x-1, y-1, newD)     
                # top right
                if y+1<n and grid[x-1][y+1]==0:
                    visitCell(x-1, y+1, newD)
            # bottom
            if x+1<n:
                if grid[x+1][y] == 0:
                    visitCell(x+1, y, newD)
                if y-1>=0 and grid[x+1][y-1]==0:
                    visitCell(x+1, y-1, newD)
                if y+1<n and grid[x+1][y+1]==0:
                    visitCell(x+1, y+1, newD)
            # left
            if y-1>=0 and grid[x][y-1]==0:
                visitCell(x, y-1, newD)
            # right
            if y+1<n and grid[x][y+1]==0:
                visitCell(x, y+1, newD)
        return -1 if distance[n-1][n-1]==inf else distance[-1][-1]
# @lc code=end

