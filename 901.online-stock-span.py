#
# @lc app=leetcode id=901 lang=python3
#
# [901] Online Stock Span
#

# @lc code=start
from collections import deque


class StockSpanner:
    def __init__(self):
        self.history = deque([])  # (value, span) pair

    def next(self, price: int) -> int:
        # for new price,
        # keep popping the self.history stack until the top item's value is larger
        # counting the span, then append and return
        span = 1
        while self.history and self.history[-1][0] <= price:
            span += self.history.pop()[1]
        self.history.append((price, span))
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
# @lc code=end
