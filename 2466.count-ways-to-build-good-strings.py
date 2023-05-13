#
# @lc app=leetcode id=2466 lang=python3
#
# [2466] Count Ways To Build Good Strings
#

# @lc code=start
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        # 1-d dp problem
        # create a 1d table, dp
        # dp[i] means the # of good strings which has length == i
        # optimal substructure: dp[i] = dp[i-zero] + dp[i-one]
        dp = [0] * (high+1)
        dp[zero]+=1
        dp[one]+=1
        for i in range(high+1):
            dp[i] += dp[i-zero] if i-zero>=0 else 0
            dp[i] += dp[i-one] if i-one>=0 else 0
        c = 0
        for i in range(low, high+1):
            c+=dp[i]
        return c%(10**9+7)
# @lc code=end


