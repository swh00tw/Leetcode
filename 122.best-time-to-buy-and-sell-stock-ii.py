#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # since now, we can buy/sell infinity times
        # to maximize the max profit, we must catch any opportunity to profit
        # we need to catch any upward trend in array
        profit = 0
        n = len(prices)
        for i in range(1, n):
            isDropping = prices[i] < prices[i - 1]
            if not isDropping:
                profit += prices[i] - prices[i - 1]
        return profit


# @lc code=end
