#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#


# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        l, r = 0, n - 1
        while l <= r and l < n and r >= 0:
            leftChar = self.getChar(s[l])
            if not leftChar:
                l += 1
                continue
            rightChar = self.getChar(s[r])
            if not rightChar:
                r -= 1
                continue

            if leftChar != rightChar:
                return False
            l += 1
            r -= 1
        return True

    def getChar(self, char):
        if "a" <= char <= "z":
            return char
        if "A" <= char <= "Z":
            return char.lower()
        if char.isnumeric():
            return char

        return None


# @lc code=end
