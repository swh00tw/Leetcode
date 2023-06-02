#
# @lc app=leetcode id=1657 lang=python3
#
# [1657] Determine if Two Strings Are Close
#

# @lc code=start
from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # the set of char should be the same
        charSet = set()
        for c in word1:
            charSet.add(c)
        for c in word2:
            if c not in charSet:
                return False
        # the freq set should be the same
        freq1 = Counter(word1)
        freq2 = Counter(word2)
        f1 = sorted(freq1.values())
        f2 = sorted(freq2.values())
        if f1!=f2:
            return False
        return True

        
# @lc code=end

