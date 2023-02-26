#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#

# @lc code=start

# The concept is alike as the Longest Common Substring problem
# use bottom up DP, the goal is to find minDistance[m,n] (m = len(x), n = len(y))
# (minDistance[i, j] is minDistance between x[:i] and y[:j])
# Optimal substructure:
# minDistamce[i,j] = minDistance[i-1, j-1] if xi == yj
# else, minDistance[i,j] = min(
#                           minDistance[i - 1][j] + 1,       # insert
#                           minDistance[i][j - 1] + 1,       # delete
#                           minDistance[i - 1][j - 1] + 1    # replace
#                           )

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # base case - i steps away
        for i in range(1, m + 1):
            dp[i][0] = i
        for j in range(1, n + 1):
            dp[0][j] = j
        # each step has four possibilities
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # same character, i and j move ahead together
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                # find min of insert, replace, remove a character
                else:
                    dp[i][j] = min(
                        dp[i - 1][j] + 1,
                        dp[i][j - 1] + 1,
                        dp[i - 1][j - 1] + 1
                    )
        
        return dp[m][n]

        
# @lc code=end

