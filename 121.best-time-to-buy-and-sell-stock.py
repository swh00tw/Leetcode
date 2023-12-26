#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        best = 0
        lowest = float("inf")
        for p in prices:
            if p >= lowest:
                best = max(best, p - lowest)
            else:
                lowest = p
        return best


# @lc code=end
