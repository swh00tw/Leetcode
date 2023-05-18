#
# @lc app=leetcode id=926 lang=python3
#
# [926] Flip String to Monotone Increasing
#

# @lc code=start
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n+1)
        numOfOnes = 0
        for i in range(1,n+1):
            newbit = s[i-1]
            if newbit == '1':
                dp[i] = dp[i-1]
                numOfOnes += 1
            else:
                dp[i] = min(dp[i-1]+1, numOfOnes)
        return dp[-1]
        
# @lc code=end

