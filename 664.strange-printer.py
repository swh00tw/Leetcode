#
# @lc app=leetcode id=664 lang=python3
#
# [664] Strange Printer
#


# @lc code=start
from functools import lru_cache


class Solution:
    def strangePrinter(self, s: str) -> int:
        # preprocess (optional)
        # eliminate consecutive charactars
        prev = s[0]
        ns = s[0]
        for c in s[1:]:
            if c == prev:
                continue
            else:
                ns += c
                prev = c
        s = ns

        @lru_cache(None)
        def dp(start, end):
            if start > end:
                return 0

            firstLetter = s[start]
            # worst case answer, firstLetter is not appearing in rest of the string
            answer = 1 + dp(start + 1, end)
            # other cases, first Letter is appearing in rest of the string
            # if there's repeating at index k,
            # it means we can possibly save some operations
            # by printing the firstLetter from start to index k initially
            # so inspect the possbility and see if it's better
            for k in range(start + 1, end + 1):
                if s[k] == firstLetter:
                    possibleAnswer = dp(start, k - 1) + dp(k + 1, end)
                    answer = min(answer, possibleAnswer)
            return answer

        return dp(0, len(s) - 1)


# @lc code=end
