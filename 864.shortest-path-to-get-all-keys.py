#
# @lc app=leetcode id=864 lang=python3
#
# [864] Shortest Path to Get All Keys
#

# @lc code=start
# https://leetcode.com/problems/shortest-path-to-get-all-keys/solutions/3694816/bfs-video-solution/
from collections import deque, defaultdict


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        x, y, m, n, totalKeys = -1, -1, len(grid), len(grid[0]), 0
        for i in range(m):
            for j in range(n):
                c = grid[i][j]
                if c == "@":
                    x, y = i, j
                if "a" <= c <= "f":
                    totalKeys += 1

        # the first item's binary string represent current keys
        # ex: 111111 represent "abcdef" keys
        # ex: 000000 represent initial state
        start = (0, x, y)
        queue = deque([start])
        visited = defaultdict(bool)
        visited[start] = True

        step = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                keys, i, j = queue.popleft()
                if keys == (1 << totalKeys) - 1:  # if all keys collected
                    return step

                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    newKeys = keys
                    if 0 <= ni < m and 0 <= nj < n:
                        c = grid[ni][nj]
                        if c == "#":
                            continue
                        if "a" <= c <= "f":
                            newKeys |= 1 << (
                                ord(c) - ord("a")
                            )  # shift 1 and OR newKeys
                        if "A" <= c <= "F" and not (
                            keys >> (ord(c) - ord("A")) & 1
                        ):  # if doesn't possess the key
                            continue
                        if not visited[(newKeys, ni, nj)]:
                            visited[(newKeys, ni, nj)] = True
                            queue.append((newKeys, ni, nj))
            step += 1
        return -1


# @lc code=end
