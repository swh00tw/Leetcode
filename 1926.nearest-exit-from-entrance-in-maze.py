#
# @lc app=leetcode id=1926 lang=python3
#
# [1926] Nearest Exit from Entrance in Maze
#

# @lc code=start
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        nearestExitDistance = inf
        m = len(maze[0])
        n = len(maze)
        def isExit(x, y):
            if x==entrance[0] and y==entrance[1]:
                return False
            if x==0 or x==n-1:
                return maze[x][y]=="."
            if y==0 or y==m-1:
                return maze[x][y]=="." 
        # bfs
        distance = [[inf]*m for _ in range(n)]
        distance[entrance[0]][entrance[1]] = 0
        def isUnvisitedCell(x, y):
            return maze[x][y]=="." and distance[x][y]==inf
        q = [entrance]
        while q:
            x, y = q.pop(0)
            if isExit(x, y):
                nearestExitDistance = min(nearestExitDistance, distance[x][y])
            # up
            if x-1>=0 and isUnvisitedCell(x-1, y):
                distance[x-1][y] = distance[x][y]+1
                q.append([x-1, y])
            # down
            if x+1<n and isUnvisitedCell(x+1, y):
                distance[x+1][y] = distance[x][y]+1
                q.append([x+1, y])
            # left
            if y-1>=0 and isUnvisitedCell(x, y-1):
                distance[x][y-1] = distance[x][y]+1
                q.append([x, y-1])
            # right
            if y+1<m and isUnvisitedCell(x, y+1):
                distance[x][y+1] = distance[x][y]+1
                q.append([x, y+1])
        return nearestExitDistance if nearestExitDistance!=inf else -1
                
# @lc code=end

