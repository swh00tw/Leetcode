#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#


# @lc code=start
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        ans = [[inf] * m for _ in range(n)]

        batch = set()
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    batch.add((i, j))
                    ans[i][j] = 0

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while len(batch) > 0:
            # keep processing block in batch
            # if it has neighbors which is 1, and undiscovered, update it's value by adding 1,
            # and push it in new batch if it's not in new batch
            newBatch = set()
            queue = list(batch)
            while queue:
                x, y = queue.pop(0)
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if (
                        0 <= nx < n
                        and 0 <= ny < m
                        and mat[nx][ny] == 1
                        and ans[nx][ny] == inf
                    ):
                        ans[nx][ny] = min(ans[nx][ny], ans[x][y] + 1)
                        if (nx, ny) not in newBatch:
                            newBatch.add((nx, ny))

            batch = newBatch

        return ans


# @lc code=end
