#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#


# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # run two binary search
        # first search which row
        # then search col
        firstNums = [row[0] for row in matrix]
        # get which row
        l, r = 0, len(firstNums) - 1
        while l <= r:
            mid = (l + r) // 2
            midNum = firstNums[mid]
            if midNum == target:
                return True
            if midNum > target:
                r = mid - 1
            else:
                l = mid + 1
        rowIdx = r
        if rowIdx < 0:
            return False
        # search in rows
        row = matrix[rowIdx]
        l, r = 0, len(row) - 1
        while l <= r:
            mid = (l + r) // 2
            if row[mid] == target:
                return True
            if row[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False


# @lc code=end
