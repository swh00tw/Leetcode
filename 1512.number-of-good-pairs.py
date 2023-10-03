#
# @lc app=leetcode id=1512 lang=python3
#
# [1512] Number of Good Pairs
#

# @lc code=start
from collections import Counter


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # O(n)
        # use a dictionary to map from number to how many number that is behind current index
        # use a for loop, from index 0 to the end, each step, do these
        # numFreqBehind[num] should decrease by one
        # answer should increment numFreqBehind[num]
        numFreqBehind = Counter(nums)
        ans = 0
        for n in nums:
            numFreqBehind[n] -= 1
            ans += numFreqBehind[n]
        return ans


# @lc code=end
