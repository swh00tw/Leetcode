#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#


# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # base case
        if n == k:
            return [[i + 1 for i in range(k)]]
        if k == 1:
            return [[i + 1] for i in range(n)]

        return self.combine(n - 1, k) + [
            subanswer + [n] for subanswer in self.combine(n - 1, k - 1)
        ]


# @lc code=end
