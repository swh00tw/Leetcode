#
# @lc app=leetcode id=1582 lang=python3
#
# [1582] Special Positions in a Binary Matrix
#


# @lc code=start
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        # rowOneFreq, key: row index, value: frequency of 1 in the row
        # colOneFreq, key: col index, value: frequency of 1 in the col
        rowOneFreq, colOneFreq = {}, {}
        n = len(mat)
        m = len(mat[0])
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    rowOneFreq[i] = rowOneFreq.get(i, 0) + 1
                    colOneFreq[j] = colOneFreq.get(j, 0) + 1
        ans = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1 and rowOneFreq[i] == 1 and colOneFreq[j] == 1:
                    ans += 1
        return ans


# @lc code=end
