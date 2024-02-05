#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#


# @lc code=start
from collections import deque


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # traverse each cell in the board,
        # each we find unvisited "O", do BFS and only traverse unvisited "O"
        # when running BFS, use a list to store all (i, j) we find
        # and use a flag to keep track of whether we should flip or not
        n = len(board)
        m = len(board[0])

        def onBoundary(position):
            x, y = position
            return (x == 0 or x == n - 1) or (y == 0 or y == m - 1)

        visited = [[False] * m for _ in range(n)]
        deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for i in range(n):
            for j in range(m):
                if board[i][j] == "X" or visited[i][j] is True:
                    continue
                shouldFlip = True
                seen = []  # store (x, y)

                queue = deque([(i, j)])
                visited[i][j] = True
                seen.append((i, j))
                while queue:
                    x, y = queue.popleft()
                    if onBoundary((x, y)):
                        shouldFlip = False
                    for dx, dy in deltas:
                        nx, ny = x + dx, y + dy
                        if (
                            0 <= nx < n
                            and 0 <= ny < m
                            and board[nx][ny] == "O"
                            and visited[nx][ny] is False
                        ):
                            visited[nx][ny] = True
                            queue.append((nx, ny))
                            seen.append((nx, ny))
                # flip
                if shouldFlip:
                    for x, y in seen:
                        board[x][y] = "X"


# @lc code=end
