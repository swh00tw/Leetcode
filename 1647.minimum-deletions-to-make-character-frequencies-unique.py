#
# @lc app=leetcode id=1647 lang=python3
#
# [1647] Minimum Deletions to Make Character Frequencies Unique
#

# @lc code=start
from collections import Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        chars = Counter(s)
        freqArray = []
        for v in chars.values():
            freqArray.append(v)
        freqArray.sort(reverse=True)
        count = 0
        freqSet = set()
        for freq in freqArray:
            if freq not in freqSet:
                freqSet.add(freq)
            else:
                newFreq = freq - 1
                while newFreq in freqSet:
                    newFreq -= 1
                count += freq - newFreq
                if newFreq > 0:
                    freqSet.add(newFreq)
        return count


# @lc code=end
