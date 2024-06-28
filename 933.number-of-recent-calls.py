#
# @lc app=leetcode id=933 lang=python3
#
# [933] Number of Recent Calls
#


# @lc code=start
from collections import deque


class RecentCounter:

    def __init__(self):
        # init a queue store timestamp for each past request
        self.pastReq = deque([])

    def ping(self, t: int) -> int:
        # push to pastReq
        # keep popping the first item if it's expired (<t-3000)
        self.pastReq.append(t)
        while self.pastReq and t - 3000 > self.pastReq[0]:
            self.pastReq.popleft()
        return len(self.pastReq)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
# @lc code=end
