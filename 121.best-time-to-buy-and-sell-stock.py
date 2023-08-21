#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        ans = 0
        minPrice = prices[0]
        for p in prices[1:]:
            profit = p - minPrice
            if profit > ans:
                ans = profit
            if p < minPrice:
                minPrice = p
        return ans


# @lc code=end
