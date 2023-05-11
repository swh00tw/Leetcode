#
# @lc app=leetcode id=1035 lang=python3
#
# [1035] Uncrossed Lines
#

# @lc code=start
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        # 2d dynamic prgramming problem
        # dp[0...n][0...m], n = len(nums1), m = len(nums2)
        # dp[i][j] means the answer for nums[:i+1] and nums[0:j+1] (i means we pick the first i numbers from nums1)
        # the final answer is dp[n][m]
        # dp[i][j] = 0 if i==0 or j==0
        # else, if nums[i]==nums[j], dp[i][j] = 1+dp[i-1][j-1]
        #       else, dp[i][j] = max(dp[i-1][j] or dp[i][j-1])
        n = len(nums1)
        m = len(nums2)
        dp = [[0]*(m+1) for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                if nums1[i-1]==nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[n][m]
# @lc code=end

