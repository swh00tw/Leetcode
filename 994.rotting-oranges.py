#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

# @lc code=start
# faster sol: https://leetcode.com/problems/rotting-oranges/solutions/563686/python-clean-well-explained-faster-than-90/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # BFS from each rotten orange as source
        # create a m x n table to store the time that orange got rotten
        self.m = len(grid[0])
        self.n = len(grid)
        self.grid = grid

        self.rottenTime = [[inf]*self.m for _ in range(self.n)]
        self.rottenOranges = []
        totalOranges = 0
        for i in range(self.n):
            for j in range(self.m):
                if grid[i][j]!=0:
                    totalOranges+=1
                if grid[i][j]==2:
                    self.rottenOranges.append((i, j))
        if totalOranges==0:
            return 0
        for src in self.rottenOranges:
            self.BFS(src)
        ans = -1
        for i in range(self.n):
            for j in range(self.m):
                if grid[i][j]!=0:
                    if self.rottenTime[i][j]==inf:
                        return -1
                    ans = max(ans, self.rottenTime[i][j])
        return ans
                

    def BFS(self, src):
        distance = [[inf]*self.m for _ in range(self.n)]
        distance[src[0]][src[1]] = 0
        q = [src]
        adj = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q:
            x, y = q.pop(0)
            # if it can update self.rottenTime successfully, keep going, else, early stop
            if distance[x][y]<self.rottenTime[x][y]:
                self.rottenTime[x][y] = distance[x][y]
                for i, j in adj:
                    if 0<=x+i<self.n and 0<=y+j<self.m and self.grid[x+i][y+j]!=0 and distance[x+i][y+j]==inf:
                        distance[x+i][y+j] = distance[x][y]+1
                        q.append((x+i, y+j))
        
# @lc code=end

