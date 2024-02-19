#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#


# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        if n < 1 or n % 2 == 1:
            return False
        return self.isPowerOfTwo(n / 2)


# @lc code=end
