#
# @lc app=leetcode id=2551 lang=python3
#
# [2551] Put Marbles in Bags
#


# @lc code=start
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:
            return 0
        n = len(weights)
        cutCosts = [(weights[i] + weights[i - 1]) for i in range(1, n)]
        cutCosts = sorted(cutCosts)
        diff = 0
        for i in range(k - 1):
            diff += cutCosts[len(cutCosts) - 1 - i]
            diff -= cutCosts[i]
        return diff


# @lc code=end
