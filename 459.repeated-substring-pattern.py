#
# @lc app=leetcode id=459 lang=python3
#
# [459] Repeated Substring Pattern
#

# @lc code=start
from collections import Counter


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) == 1:
            return False
        if len(Counter(s)) == 1:
            return True
        n = len(s)
        for substringLength in range(2, n // 2 + 1):
            if n % substringLength != 0:
                continue
            substr = s[:substringLength]
            ss = s[:]
            while len(ss) > 0:
                if ss[:substringLength] == substr:
                    ss = ss[substringLength:]
                else:
                    break
            if len(ss) == 0:
                return True

        return False


# @lc code=end
