#
# @lc app=leetcode id=1218 lang=python3
#
# [1218] Longest Arithmetic Subsequence of Given Difference
#


# @lc code=start
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        # reverse 1-dp
        # dp[i] means the longest subsequence starting from arr[i] (included)
        # use a var to keep track of longest
        longest = -1
        n = len(arr)
        dp = [0] * n
        numToIdx = {}
        for i in range(n - 1, -1, -1):
            num = arr[i]
            if numToIdx.get(num + difference):
                dp[i] = 1 + dp[numToIdx[num + difference]]
            else:
                dp[i] = 1
            numToIdx[num] = i
            longest = max(longest, dp[i])
        return longest


# @lc code=end
