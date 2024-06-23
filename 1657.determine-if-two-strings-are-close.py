#
# @lc app=leetcode id=1657 lang=python3
#
# [1657] Determine if Two Strings Are Close
#

# @lc code=start
from collections import Counter, defaultdict


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # use hashmap, (counter)
        # if different length or different set of characters, return false
        # if two strings have the same character frequency, return true
        # Ex: {a: 3, b: 2, c: 1} / {b: 3, c: 1, a: 2} --> true
        # produce reverse map: {1: 1, 2: 1, 3: 1} (map from freq to how many character)
        # check the length of each entry is the same
        if len(word1) != len(word2):
            return False
        freq1 = Counter(word1)
        freq2 = Counter(word2)
        for c in freq1:
            if c not in freq2:
                return False
        for c in freq2:
            if c not in freq1:
                return False
        rev_map1 = defaultdict(int)
        rev_map2 = defaultdict(int)
        for v in freq1.values():
            rev_map1[v] += 1
        for v in freq2.values():
            rev_map2[v] += 1
        for k in rev_map1:
            if rev_map1[k] != rev_map2[k]:
                return False
        return True


# @lc code=end
