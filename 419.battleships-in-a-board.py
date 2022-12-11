#
# @lc app=leetcode id=419 lang=python3
#
# [419] Battleships in a Board
#

# @lc code=start
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        shipsCounter = 0
        
        for y in range(len(board)):
            for x in range(len(board[0])):
                isShipHere = board[y][x] == "X"
                isShipLeft = False  
                isShipAbove = False

                if x > 0: 
                    isShipLeft = board[y][x-1] == "X"
                if y > 0: 
                    isShipAbove = board[y-1][x] == "X"
                
                if isShipHere and not isShipLeft and not isShipAbove:
                    shipsCounter += 1
                
        return shipsCounter

    def countBattleships2(self, board: List[List[str]]) -> int:
        # find 1*k, k>1
        horizontal = 0
        for row in board:
            rowString = ''.join(row)
            ships = rowString.split('.')
            for ship in ships:
                if self.isShip(ship) and len(ship)>1:
                    horizontal+=1
        print(f"horizontal: {horizontal}")
        # find k*1, k>1
        transposeMatrix = self.transpose2Darray(board)
        vertical = 0
        for col in transposeMatrix:
            colString = ''.join(col)
            ships = colString.split('.')
            for ship in ships:
                if self.isShip(ship) and len(ship)>1:
                    vertical+=1
        print(f"vertical: {vertical}")
        # find 1*1
        smallest = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=="X":
                    # if has top, check if it's 'X'
                    if i>0 and board[i-1][j]=="X":
                        continue
                    # if has left, check if it's 'X'
                    if j>0 and board[i][j-1]=="X":
                        continue
                    # if has right, check if it's 'X'
                    if j<len(board[0])-1 and board[i][j+1]=="X":
                        continue
                    # if has bottom, check if it's 'X'
                    if i<len(board)-1 and board[i+1][j]=="X":
                        continue
                    smallest +=1
        print(f"smallest: {smallest}")

        return horizontal+vertical+smallest

    def isShip(self, str):
        for i in str:
            if i!='X':
                return False
        return True

    def transpose2Darray(self, theArray):
        return [list(i) for i in zip(*theArray)]
        
# @lc code=end

