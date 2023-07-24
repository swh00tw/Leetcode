#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#


# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = self.calculatePow(x, abs(n))
        if n >= 0:
            return res
        else:
            return 1 / res

    def calculatePow(self, x, n):
        if x == 0:
            return 0
        if n == 0:
            return 1
        if n == 1:
            return x

        ans = 1 if n % 2 == 0 else x
        num = n if n % 2 == 0 else n - 1
        tmp = self.myPow(x, num / 2)
        return ans * tmp * tmp


# @lc code=end
