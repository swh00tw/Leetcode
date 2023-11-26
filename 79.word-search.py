#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#


# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # for each cell in the matrix
        # we run DFS from there
        # return True if we found it
        # return false
        # TC: O(mnk)
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if self.search(i, j, board, word, 0):
                    return True
        return False

    def search(self, i, j, board, word, idx) -> bool:
        # out of bound
        m = len(board)
        n = len(board[0])
        if not (0 <= i < m) or not (0 <= j < n):
            return False
        # base case
        letter = board[i][j]
        if letter != word[idx]:
            return False
        if idx == len(word) - 1:
            return True
        # normal case
        ans = False
        board[i][j] = "#"
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = i + dx, j + dy
            ans = ans or self.search(nx, ny, board, word, idx + 1)
        board[i][j] = letter
        return ans


# @lc code=end
