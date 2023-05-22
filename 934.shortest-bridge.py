#
# @lc app=leetcode id=934 lang=python3
#
# [934] Shortest Bridge
#

# @lc code=start
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # find the first island by BFS
        # run BFS(Dijkstra) for any block in island
        # ignore if it's already in island
        # if find the block has value 1 and not in first island
        # we return the distance
        n = len(grid)
        visited = [[False]*n for _ in range(n)]
        firstIsland = set()
        founded = False
        for i in range(n):
            for j in range(n):
                if founded:
                    continue
                if grid[i][j]==1:
                    founded = True
                    # bfs
                    q = [(i,j)]
                    visited[i][j]=True
                    while q:
                        x, y = q.pop(0)
                        firstIsland.add((x, y))
                        if y-1>=0 and not visited[x][y-1] and grid[x][y-1]==1:
                            q.append((x, y-1))
                            visited[x][y-1]=True
                        if x-1>=0 and not visited[x-1][y] and grid[x-1][y]==1:
                            q.append((x-1, y))
                            visited[x-1][y]=True
                        if y+1<n and not visited[x][y+1] and grid[x][y+1]==1:
                            q.append((x, y+1))
                            visited[x][y+1]=True
                        if x+1<n and not visited[x+1][y] and grid[x+1][y]==1:
                            q.append((x+1,y))
                            visited[x+1][y]=True
                    
        q=list(firstIsland)
        visited = [[False]*n for _ in range(n)]
        for x, y in q:
            visited[x][y]=True
        while q:
            x, y = q.pop(0)
            if y-1>=0 and not visited[x][y-1]:
                q.append((x, y-1))
                visited[x][y-1]=True
                if (x, y-1) not in firstIsland:
                    if grid[x][y-1]==1:
                        return grid[x][y]-1
                    if grid[x][y-1]==0:
                        grid[x][y-1]=grid[x][y]+1
                    else:
                        grid[x][y-1]=min(grid[x][y]+1, grid[x][y-1])
            if x-1>=0 and not visited[x-1][y]:
                q.append((x-1, y))
                visited[x-1][y]=True
                if (x-1, y) not in firstIsland:
                    if grid[x-1][y]==1:
                        return grid[x][y]-1
                    if grid[x-1][y]==0:
                        grid[x-1][y]=grid[x][y]+1
                    else:
                        grid[x-1][y]=min(grid[x][y]+1, grid[x-1][y])
            if y+1<n and not visited[x][y+1]:
                q.append((x, y+1))
                visited[x][y+1]=True
                if (x, y+1) not in firstIsland:
                    if grid[x][y+1]==1:
                        return grid[x][y]-1
                    if grid[x][y+1]==0:
                        grid[x][y+1]=grid[x][y]+1
                    else:
                        grid[x][y+1]=min(grid[x][y]+1, grid[x][y+1])
            if x+1<n and not visited[x+1][y]:
                q.append((x+1,y))
                visited[x+1][y]=True
                if (x+1, y) not in firstIsland:
                    if grid[x+1][y]==1:
                        return grid[x][y]-1
                    if grid[x+1][y]==0:
                        grid[x+1][y]=grid[x][y]+1
                    else:
                        grid[x+1][y]=min(grid[x][y]+1, grid[x+1][y])
        
# @lc code=end

