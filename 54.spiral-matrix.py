#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def __init__(self):
        self.directionIdx = 0
    def updateDirection(self):
        self.directionIdx = (self.directionIdx+1)%4
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        res = []
        added = [[False]*n for _ in range(m)]
        
        i, j = 0, 0
        while len(res)!= m*n:
            # add to list
            res.append(matrix[i][j])
            added[i][j] = True
            # determine next direction
            # if index out of range or point to an added number, change direction
            if self.directionIdx == 0: # goRight
                nextI, nextJ = i, j+1
                if nextJ>=n or added[nextI][nextJ] == True:
                    nextI, nextJ = i+1, j
                    self.updateDirection()
            elif self.directionIdx == 1: #goDown
                nextI, nextJ = i+1, j
                if nextI>=m or added[nextI][nextJ] == True:
                    nextI, nextJ = i, j-1
                    self.updateDirection()
            elif self.directionIdx == 2: #goLeft
                nextI, nextJ = i, j-1
                if nextJ<0 or added[nextI][nextJ] == True:
                    nextI, nextJ = i-1, j
                    self.updateDirection()
            else: #goUp
                nextI, nextJ = i-1, j
                if nextI<0 or added[nextI][nextJ] == True:
                    nextI, nextJ = i, j+1
                    self.updateDirection()
            i, j = nextI, nextJ
        return res



        
# @lc code=end

