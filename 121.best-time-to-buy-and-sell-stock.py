#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        lowest = prices[0]
        maximum = 0

        for i, price in enumerate(prices[1:]):
            # update maximum
            if price - lowest > maximum:
                maximum = price - lowest
            # update lowest
            if price < lowest:
                lowest = price
        
        return maximum
# @lc code=end

