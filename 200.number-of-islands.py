#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#


# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # run BFS for unvisited cells (value is "1" && not visited)
        #     while running, mark cell as visited when the value of cell is "1"
        # count how many island
        deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        n = len(grid)
        m = len(grid[0])
        islands = 0
        visited = [[False] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                # if not visited and value is "1"
                if grid[i][j] == "1" and not visited[i][j]:
                    islands += 1
                    # BFS
                    queue = [(i, j)]
                    visited[i][j] = True
                    while queue:
                        x, y = queue.pop(0)
                        for dx, dy in deltas:
                            nx, ny = x + dx, y + dy
                            if (
                                0 <= nx < n
                                and 0 <= ny < m
                                and grid[nx][ny] == "1"
                                and not visited[nx][ny]
                            ):
                                visited[nx][ny] = True
                                queue.append((nx, ny))
        return islands


# @lc code=end
