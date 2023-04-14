#
# @lc app=leetcode id=516 lang=python3
#
# [516] Longest Palindromic Subsequence
#

# @lc code=start
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        if n==1:
            return 1
        dp = [[0]*n for i in range(n)]
        # base condition
        for i in range(n):
            dp[i][i] = 1
        # fill the table
        # dp[i][j] means the length of longest subseq of s[i:j]
        # optimal substructure:
        # dp[i][j] = if s[i]==s[j], dp[i+1][j-1]+2
        #            else, max(dp[i+1][j], dp[i][j-1])
        for x in range(1,n):
            for i in range(n-x):
                j = i + x
                if s[i]==s[j]:
                    dp[i][j] = dp[i+1][j-1]+2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][n-1]

        
# @lc code=end

