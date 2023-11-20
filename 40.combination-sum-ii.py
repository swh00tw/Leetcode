#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#


# @lc code=start
from collections import Counter


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # construct a recursive function getCombination(idx, target) -> List[List[int]]
        # this function will return all combination whose sum is target using candidates[idx:]
        # recursive relation
        # 1. use the candidates[idx] (use 1, 2, ..., k, ... freq[candidates[idx]])
        # --> candidates[idx]*k + getCombination(idx+1, target-candidates[idx])
        # 2. do not use candidates[idx] --> getCombination(idx+1, target])
        # base case: if target < 0 --> return []
        candidates.sort()
        freq = Counter(candidates)
        seen = set()
        tmp = []
        for num in candidates:
            if num not in seen:
                seen.add(num)
                tmp.append(num)
        candidates = tmp

        def getCombination(idx, target):
            if idx >= len(candidates):
                return []
            n = candidates[idx]
            if target < n:
                return []

            combinations = []
            # 1.
            for i in range(1, freq[n] + 1):
                if target - n * i == 0:
                    combinations.append([n] * i)
                else:
                    for comb in getCombination(idx + 1, target - n * i):
                        combinations.append([n] * i + comb)

            # 2.
            for comb in getCombination(idx + 1, target):
                combinations.append(comb)

            return combinations

        return getCombination(0, target)


# @lc code=end
