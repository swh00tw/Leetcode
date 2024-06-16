#
# @lc app=leetcode id=1456 lang=python3
#
# [1456] Maximum Number of Vowels in a Substring of Given Length
#


# @lc code=start


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # sliding window
        # need a function isVowel
        # keep track of current numVowels and bestAns
        numVowels = 0
        bestAns = 0
        n = len(s)
        for i in range(k):
            if self.isVowel(s[i]):
                numVowels += 1
        if n == k:
            return numVowels
        bestAns = numVowels
        for i in range(k, n):
            if self.isVowel(s[i]):
                numVowels += 1
            if self.isVowel(s[i - k]):
                numVowels -= 1
            bestAns = max(bestAns, numVowels)
        return bestAns

    def isVowel(self, char):
        if len(char) > 1:
            raise Exception("the argument must be a character")
        return char in "aeiou"


# @lc code=end
