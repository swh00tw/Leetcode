#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Row
        for rowIdx in range(9):
            nums = set()
            for colIdx in range(9):
                if board[rowIdx][colIdx]!=".":
                    n = int(board[rowIdx][colIdx])
                    if n in nums:
                        return False
                    else:
                        nums.add(n)
        # Col
        for colIdx in range(9):
            nums = set()
            for rowIdx in range(9):
                if board[rowIdx][colIdx]!=".":
                    num = int(board[rowIdx][colIdx])
                    if num in nums:
                        return False
                    else:
                        nums.add(num)
        # for small box
        for rowIdx in range(0, 9, 3):
            for colIdx in range(0, 9, 3):
                nums = set()
                for i in range(rowIdx, rowIdx+3):
                    for j in range(colIdx, colIdx+3):
                        if board[i][j]!=".":
                            n = int(board[i][j])
                            if n in nums:
                                return False
                            else:
                                nums.add(n)
        return True
        
# @lc code=end

