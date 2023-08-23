#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#


# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        num = columnNumber
        ans = ""
        while num > 0:
            num, remainder = divmod(num - 1, 26)
            ans += self.num2Letter(remainder)

        return ans[::-1]

    def num2Letter(self, num):
        return chr(num + 65)


# @lc code=end
