#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#

# @lc code=start
class Solution:
    def __init__(self):
        self.direction = 0
        # 0: right
        # 1: down
        # 2: left
        # 3: up
    def updateDirection(self):
        self.direction = (self.direction+1)%4
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[-1]*n for _ in range(n)]
        num = 1
        i, j = 0, 0
        while num<=n**2:
            matrix[i][j] = num
            num+=1
            # determine next block
            if self.direction == 0:
                ni, nj = i, j+1
                if nj>=n or matrix[ni][nj]!=-1:
                    self.updateDirection()
                    ni, nj = i+1, j
            elif self.direction == 1:
                ni, nj = i+1, j
                if ni>=n or matrix[ni][nj]!=-1:
                    self.updateDirection()
                    ni, nj = i, j-1
            elif self.direction == 2:
                ni, nj = i, j-1
                if nj<0 or matrix[ni][nj]!=-1:
                    self.updateDirection()
                    ni, nj = i-1, j
            else:
                ni, nj = i-1, j
                if ni<0 or matrix[ni][nj]!=-1:
                    self.updateDirection()
                    ni, nj = i, j+1
            i, j = ni, nj
        return matrix

# @lc code=end

