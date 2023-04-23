#
# @lc app=leetcode id=1312 lang=python3
#
# [1312] Minimum Insertion Steps to Make a String Palindrome
#

# @lc code=start
class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        for x in range(1,n):
            for i in range(n-x):
                j = i+x
                substring = s[i:j+1]
                if substring[0] == substring[-1]:
                    dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + 1

        return dp[0][n-1]

        
# @lc code=end

