#
# @lc app=leetcode id=823 lang=python3
#
# [823] Binary Trees With Factors
#


# @lc code=start
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        # num in arr >= 2
        # arr.length >= 1
        # all unique

        # dp problem
        # dp(n): how many tree when root node is n
        # for a root node to grow
        # it need to find a pair of number that a*b = root
        # if it cannot find, stop growing, return 1
        # if it do find, dp[n] = dp[a]*dp[b]

        cache = {}
        nums = set(arr)

        def getNumOfTree(n: int):
            # in cache
            if n in cache:
                return cache[n]

            pairsOfFactor = []
            for num in arr:
                if n % num == 0 and n // num in nums:
                    pairsOfFactor.append([num, n // num])

            # if cannot find
            if len(pairsOfFactor) == 0:
                return 1
            ans = 1
            for a, b in pairsOfFactor:
                ans += getNumOfTree(a) * getNumOfTree(b)
                ans = ans % (10**9 + 7)
            # save to cache
            cache[n] = ans
            return ans

        return sum([getNumOfTree(n) for n in arr]) % (10**9 + 7)


# @lc code=end
