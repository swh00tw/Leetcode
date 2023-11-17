#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#


# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # we sort the candidates first
        # create a recursive function to solve this
        # we form answers in a sorted way to avoid duplication
        # the answer might start from any value in the candidates
        # for loop, i..n
        #   num = candidates[i]
        #   the answer would be the number of ways to form (target-num) using candidates[i:]
        candidates.sort()

        def solve(candidates, target):
            # base condition
            # 1. target is zero or negative
            if target <= 0:
                return []

            ans = []
            for n in candidates:
                if n == target:
                    ans.append([n])

            for i, n in enumerate(candidates):
                for subset in solve(candidates[i:], target - n):
                    ans.append([n] + subset)
            return ans

        return solve(candidates, target)


# @lc code=end
