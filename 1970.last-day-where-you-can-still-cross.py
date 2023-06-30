#
# @lc app=leetcode id=1970 lang=python3
#
# [1970] Last Day Where You Can Still Cross
#


# @lc code=start
class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        l, r = 0, len(cells) - 1
        # binary search
        # find the first day that, including that day, the grid is not crossable
        # or
        # find the last day (rightmost day) that, including that day, the grid is crossable
        while l <= r:
            mid = (l + r) // 2
            if self.canCross(cells[: mid + 1], row, col):
                l = mid + 1
            else:
                r = mid - 1
        return l

    def canCross(self, cells, row, col):
        grid = [[0] * col for _ in range(row)]
        for x, y in cells:
            grid[x - 1][y - 1] = 1
        # bfs
        visited = [[False] * col for _ in range(row)]
        queue = []
        for c in range(col):
            if grid[0][c] == 0:
                queue.append((0, c))
                visited[0][c] = True
        delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while queue:
            nextQueue = []
            for x, y in queue:
                if x == row - 1:
                    return True
                for dx, dy in delta:
                    nx, ny = x + dx, y + dy
                    if (
                        (0 <= nx < row and 0 <= ny < col)
                        and not visited[nx][ny]
                        and grid[nx][ny] == 0
                    ):
                        visited[nx][ny] = True
                        nextQueue.append((nx, ny))
            queue = nextQueue
        return False


# @lc code=end
