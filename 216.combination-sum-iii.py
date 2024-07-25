#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#


# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # always return in increasing order
        return self.findCombinations(n, k, 1, 9)

    def findCombinations(self, target, k, lower, upper):
        if target <= 0:
            return []
        # we can only use number from lower to upper bound
        if k == 1:
            if lower <= target <= upper:
                return [[target]]
            return []
        res = []
        for i in range(lower, upper + 1):
            combinations = self.findCombinations(target - i, k - 1, i + 1, upper)
            res += [[i] + comb for comb in combinations]
        return res


# @lc code=end
