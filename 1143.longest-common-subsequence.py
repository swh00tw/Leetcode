#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 2d dp
        # dp[i][j] is the length of LCS of text1[:i] and text2[:j]
        # dp[i][j] = dp[i-1][j-1]+1 if text1[i]==text2[j]
        # else, dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        m = len(text1)
        n = len(text2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return dp[m][n]
        
# @lc code=end

