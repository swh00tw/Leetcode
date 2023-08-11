#
# @lc app=leetcode id=518 lang=python3
#
# [518] Coin Change II
#


# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp
        dp = [1] + [0] * amount
        for c in coins:
            for i in range(c, len(dp)):
                dp[i] += dp[i - c] if i - c >= 0 else 0
        return dp[-1]


# @lc code=end
