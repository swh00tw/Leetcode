#
# @lc app=leetcode id=1071 lang=python3
#
# [1071] Greatest Common Divisor of Strings
#

# @lc code=start
from math import gcd, lcm
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 == str2:
            return str1
        short = str2 if len(str2)<len(str1) else str1
        long = str1 if len(str2)<len(str1) else str2
        lcmLength = lcm(len(short), len(long))
        for i in range(lcmLength):
            if short[i%len(short)]!=long[i%len(long)]:
                return ""
        return long[:gcd(len(long), len(short))]

# @lc code=end

