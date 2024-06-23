#
# @lc app=leetcode id=1207 lang=python3
#
# [1207] Unique Number of Occurrences
#

# @lc code=start
from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = Counter(arr)
        numSet = set()
        for v in freq.values():
            if v in numSet:
                return False
            numSet.add(v)
        return True


# @lc code=end
