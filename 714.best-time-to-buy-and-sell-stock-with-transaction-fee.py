#
# @lc app=leetcode id=714 lang=python3
#
# [714] Best Time to Buy and Sell Stock with Transaction Fee
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # 1d dp problem
        # create two array, free & hold
        # free[i] represent the maximum profit can gain on the i-th day without holding stock
        # hold[i] represent the maximum profit can gain on the i-th day with stock holding
        # optimal substructure
        # free[i] = hold[i-1]+prices[i]-fee (selling on i-th day) OR free[i-1] (no sell on i-th day)
        # hold[i] = free[i-1]-prices[i] (buying on i-th day) OR hold[i-1] (no buy on i-th day)
        # base case:
        # free[0] = 0
        # hold[0] = -prices[0]
        n =len(prices)
        free = [0]*n
        hold = [0]*n
        hold[0] = -prices[0]
        for i in range(1, n):
            free[i] = max(free[i-1], hold[i-1]+prices[i]-fee)
            hold[i] = max(hold[i-1], free[i-1]-prices[i])
        return free[-1]
        
# @lc code=end

