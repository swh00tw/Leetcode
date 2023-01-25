#
# @lc app=leetcode id=909 lang=python3
#
# [909] Snakes and Ladders
#

# @lc code=start
class Cell:
    def __init__(self, number, adj):
        self.adj = adj
        self.d = -1 # step from source, -1 means not reachable
        self.status = "unvisited" # "discovered", "visited"

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # parse board to a hashmap
        ladderOrSnake = {}
        cells = {}
        cellIndex = 1
        reversedParse = False
        boardReverse = board[::-1]
        for i in range(len(boardReverse)):
            row = boardReverse[i]
            if reversedParse:
                row = row[::-1]
            for j in range(len(row)):
                cellTarget = row[j] if row[j]!=-1 else None
                if cellTarget:
                    ladderOrSnake[cellIndex] = cellTarget
                cellNumber = cellIndex
                cellIndex+=1
                adj = [i for i in range(cellNumber+1, cellNumber+7) if i<=len(board)**2]
                cells[cellNumber] = Cell(cellNumber, adj)
            reversedParse = not reversedParse
        # shortest path problem
        # sol1: BFS
        # KEY: if adj contain some ladder or snake, replace it with the target
        # because they are same node
        for key in cells:
            for i in range(len(cells[key].adj)):
                if cells[key].adj[i] in ladderOrSnake:
                    cells[key].adj[i] = ladderOrSnake[cells[key].adj[i]]
        cells[1].d = 0
        cells[1].status = "discovered"
        queue = [cells[1]]
        while queue:
            c = queue.pop(0)
            for adj in c.adj:
                if cells[adj].status == "unvisited":
                    cells[adj].d = c.d+1
                    cells[adj].status = "discovered"
                    queue.append(cells[adj])
            c.status = "visited"
        return cells[len(board)**2].d
        # sol2: Dijkstra
        # we treat ladder and snake as vertex with weight 0
        # and the rest as vertex with weight 1
        # TODO: implement Dijkstra

        
# @lc code=end

