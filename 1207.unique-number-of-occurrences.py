#
# @lc app=leetcode id=1207 lang=python3
#
# [1207] Unique Number of Occurrences
#

# @lc code=start
from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        freq = set()
        for v in counter.values():
            if v in freq:
                return False
            freq.add(v)
        return True
        
# @lc code=end

