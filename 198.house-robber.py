#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        # maximum value of robbing[i] would be derived from dp[i+2] & dp[i+3] (no dp[i+4] since it's always lower than dp[i+2])
        n = len(nums)
        dp =[0]*n
        for i in range(n-1, -1, -1):
            dp[i] = nums[i]+(max(dp[i+2] if i+2<n else 0, dp[i+3] if i+3<n else 0))
        return max(dp[0], dp[1] if n>1 else -1)

# @lc code=end

