#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
from collections import defaultdict


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = defaultdict(list)
        for w in wordDict:
            words[w[0]].append(w)
        cache = {}

        # recursive
        def getAns(s: str, wordDict: defaultdict[str, List[str]]) -> bool:
            if len(s) == 0:
                return True
            if s in cache:
                return cache[s]
            candidiates = wordDict[s[0]]
            for c in candidiates:
                if s == c:
                    cache[s] = True
                    return True
                elif s.startswith(c) and len(c) < len(s):
                    if getAns(s[len(c) :], wordDict):
                        cache[s] = True
                        return True
            cache[s] = False
            return False

        return getAns(s, words)


# @lc code=end
