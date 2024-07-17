#
# @lc app=leetcode id=1926 lang=python3
#
# [1926] Nearest Exit from Entrance in Maze
#

# @lc code=start
from collections import deque


class Maze:
    def __init__(self, map):
        self.n = len(map)
        self.m = len(map[0])
        self.map = map

    def isBoundary(self, i, j):
        if i == 0 or j == 0:
            return True
        if i == self.n - 1 or j == self.m - 1:
            return True
        return False

    def getNearestExit(self, i, j):
        # return number of steps to nearest exit
        # if no, return -1
        # bfs
        # use a variable to keep track of steps need to reach nearest entrance
        # early stop. if traverse to boundary, stop since further traveral will only increase number of steps
        ans = float("inf")
        q = deque([(i, j, 0)])
        visited = [[False] * self.m for _ in range(self.n)]
        visited[i][j] = True
        delta = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        while q:
            x, y, steps = q.popleft()
            if self.isBoundary(x, y) and (x, y) != (i, j):
                ans = min(ans, steps)
                continue
            for dx, dy in delta:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < self.n and 0 <= ny < self.m:
                    if visited[nx][ny] is False and self.map[nx][ny] == ".":
                        visited[nx][ny] = True
                        q.append((nx, ny, steps + 1))
        return ans if ans < float("inf") else -1


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = Maze(maze)
        return m.getNearestExit(entrance[0], entrance[1])


# @lc code=end
