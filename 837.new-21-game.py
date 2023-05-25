#
# @lc app=leetcode id=837 lang=python3
#
# [837] New 21 Game
#

# @lc code=start
from collections import defaultdict
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # dp problem to me
        # create a table: dp --> keep track of the probablity of each point
        # dp[i] --> probability of getting i points
        if k==0 or n>=k+maxPts: # direct end game or n is impossible to reach
            return 1.0
        dp = defaultdict(int)
        dp[0] = 1.0
        # sliding window
        prefixSum = 1
        for i in range(1, n+1):
            # if i<k, grow window right by 1, update prefixSum
            # if window is longer than maxPts, remove one in the front of window, update prefixSum
            dp[i] = prefixSum*(1/maxPts)
            if i<k:
                prefixSum+=dp[i]
            if i>=maxPts:
                prefixSum-=dp[i-maxPts]
        print(dp)
        return sum([dp[i] for i in range(k, n+1)])

        
# @lc code=end

