#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

# @lc code=start
# faster sol: https://leetcode.com/problems/rotting-oranges/solutions/563686/python-clean-well-explained-faster-than-90/?envType=study-plan-v2&envId=leetcode-75
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # n = len(grid)
        # m = len(grid[0])
        # count how many rotten oranges and put the rotten ones' position to an array
        # count total oranges
        # for each rotten orange, run BFS simultanenuously
        # and after BFS finish, return how many minutes past, if not all oranges become rotten, return -1
        # when we run BFS, we can keep track of the timing for each orange become rotten
        n = len(grid)
        m = len(grid[0])
        finishTime = -1
        total = 0
        rotten = 0
        q = deque([])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                    rotten += 1
                if grid[i][j] != 0:
                    total += 1
        if rotten == total:
            return 0
        graph = [[grid[x][y] for y in range(m)] for x in range(n)]
        delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            x, y, t = q.popleft()
            finishTime = max(finishTime, t)
            for dx, dy in delta:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                    graph[nx][ny] = 2
                    rotten += 1
                    q.append((nx, ny, t + 1))

        if rotten == total:
            return finishTime
        return -1
        # TC: O(mn)


# @lc code=end
