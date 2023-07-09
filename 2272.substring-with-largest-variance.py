#
# @lc app=leetcode id=2272 lang=python3
#
# [2272] Substring With Largest Variance
#


# @lc code=start
# kadane algorithm
class Solution:
    def largestVariance(self, s: str) -> int:
        if len(s) == 1 or len(s) == 2:
            return 0

        # there are 26*25 charactars pair (c1, c2)
        # use kadane algorithm to find max(c1's occurence - c2's occurence)
        # ignore charactars in substring that is neithor c1 nor c2
        # do it in reverse order again to make sure we inspect all possible substring
        best = 0
        pairs = [(c1, c2) for c1 in set(s) for c2 in set(s) if c1 != c2]
        for _ in range(2):  # original order and reverse order
            for c1, c2 in pairs:
                count1, count2 = 0, 0
                for newChar in s:
                    if newChar not in [c1, c2]:
                        continue
                    if newChar == c1:
                        count1 += 1
                    elif newChar == c2:
                        count2 += 1

                    if count1 < count2:
                        # discard current counting and start over again
                        count1, count2 = 0, 0
                    elif count1 > 0 and count2 > 0:
                        best = max(best, count1 - count2)
            s = s[::-1]  # reverse s
        return best


# @lc code=end
