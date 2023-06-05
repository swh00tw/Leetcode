#
# @lc app=leetcode id=1232 lang=python3
#
# [1232] Check If It Is a Straight Line
#

# @lc code=start
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)
        if n==2:
            return True
        slope = inf if (coordinates[1][0]-coordinates[0][0])==0 else (coordinates[1][1]-coordinates[0][1])/(coordinates[1][0]-coordinates[0][0])
        for i in range(2, n):
            curr = coordinates[i]
            prev = coordinates[i-1]
            newSlope = inf if (curr[0]-prev[0])==0 else (curr[1]-prev[1])/(curr[0]-prev[0])
            if newSlope!=slope:
                return False
        return True
# @lc code=end

