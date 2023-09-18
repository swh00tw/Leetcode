#
# @lc app=leetcode id=1337 lang=python3
#
# [1337] The K Weakest Rows in a Matrix
#


# @lc code=start
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # for each row, calculate the "score"
        # sort the (score, rowIdx) by score
        # return the first k rowIdx
        # score = m*(number of 1s) + rowIdx
        # m = number of rows
        # 0 <= rowIdx < m
        rows = [(self.getScore(mat, i), i) for i in range(len(mat))]
        rows.sort()
        return [x[1] for x in rows[:k]]

    def getScore(self, mat, rowIdx):
        return sum(mat[rowIdx]) * len(mat) + rowIdx


# @lc code=end
