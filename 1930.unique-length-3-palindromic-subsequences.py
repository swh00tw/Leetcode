#
# @lc app=leetcode id=1930 lang=python3
#
# [1930] Unique Length-3 Palindromic Subsequences
#


# @lc code=start
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # Explain:
        # the palidrome of length 3
        # can be expressed by the form of xyx, x is any letter, y is any letter
        # let x = 'a', find how many unique palindrome
        # let x = 'b', find how many
        # ...
        # let x = 'z', find how many
        # As for counting how many "unique" palindrome, we just count how many unique characters
        # in the middle of 1st appearance and last appearance
        # Steps:
        # 1. count the 1st and last appearance for each letter
        # 2. for each letter, find how many palindrome(find how many unique letters between 1st and last appearance)

        appearance = {}  # (1st, last)
        for idx, letter in enumerate(s):
            if letter not in appearance:
                appearance[letter] = (idx, idx)
            else:
                appearance[letter] = (appearance[letter][0], idx)

        count = 0
        for letter in appearance:
            first, last = appearance[letter]
            if first == last:
                continue
            # count unique letters
            uniques = 0
            letters = set()
            for i in range(first + 1, last):
                if s[i] not in letters:
                    uniques += 1
                    letters.add(s[i])
            count += uniques

        return count


# @lc code=end
