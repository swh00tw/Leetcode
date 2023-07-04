#
# @lc app=leetcode id=2305 lang=python3
#
# [2305] Fair Distribution of Cookies
#


# @lc code=start
class Solution:
    def distributeCookies(self, cookies, k):
        self.ans = float("inf")
        self.count = [0] * k

        self.backtrack(0, cookies, k)
        return self.ans

    def backtrack(self, cookieNumber, cookies, k):
        if cookieNumber == len(cookies):
            maximum = max(self.count)
            self.ans = min(self.ans, maximum)
            return

        for i in range(k):
            self.count[i] += cookies[cookieNumber]
            self.backtrack(cookieNumber + 1, cookies, k)
            self.count[i] -= cookies[cookieNumber]
            if self.count[i] == 0:
                break


# @lc code=end
