#
# @lc app=leetcode id=1027 lang=python3
#
# [1027] Longest Arithmetic Subsequence
#

# @lc code=start
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        # since the best subsequence must end between nums[0] and nums[n-1]
        # use an index i to be the end of subseq
        # for each i, we create a dictionary map "Diff" to the longest subseq's length
        # thus, the optimal substructure of dp[i][diff] = (dp?.[j]?.[diff] ?? 1) + 1, for all j in front of i
        # create a variable to keep track of longest subseq we discovered now
        n = len(nums)
        if n==2:
            return 2
        dp = [{} for _ in range(n)]
        longest = -inf
        for i in range(n):
            for j in range(i):
                diff = nums[i]-nums[j]
                dp[i][diff] = dp[j].get(diff, 1)+1
                longest = max(longest, dp[i][diff])
        return longest
        
        
# @lc code=end

