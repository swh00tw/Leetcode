#
# @lc app=leetcode id=2140 lang=python3
#
# [2140] Solving Questions With Brainpower
#

# @lc code=start
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # dp problem
        # dp[i] is the maximum points could get starting from index i, i = [0:n-1], n = len(questions)
        # answer we want is dp[0]
        # reverse order
        n = len(questions)
        dp = [0]*n
        dp[-1] = questions[-1][0]
        if n==1:
            return dp[-1]
        for i in range(n-2, -1, -1):
            # for dp[i]
            # the answer is either from including question i: questions[i][0] + dp[i+questions[i][1]]
            #                      or not including question i: dp[i+1]
            dp[i] = dp[i+1]
            points, shift = questions[i]
            dp[i] = max(dp[i], points+(dp[i+shift+1] if 0<= i+shift+1 < n else 0))
        return dp[0]

# @lc code=end

