#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#


# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while True:
            # get next l
            while l < len(s) and not s[l].isalnum():
                l += 1
            # get next r
            while r > 0 and not s[r].isalnum():
                r -= 1
            if l > r:
                return True

            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True


# @lc code=end
