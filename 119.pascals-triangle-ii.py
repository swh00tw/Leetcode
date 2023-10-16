#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#


# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        if rowIndex == 0:
            return row
        for _ in range(rowIndex):
            newRow = [1]
            for i in range(len(row)):
                newNum = row[i]
                if i + 1 < len(row):
                    newNum += row[i + 1]
                newRow.append(newNum)
            row = newRow
        return row


# @lc code=end
