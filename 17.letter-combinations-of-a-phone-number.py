#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#


# @lc code=start
class Solution:
    def __init__(self):
        self.digitCharMap = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz",
        }

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        firstDigit = int(digits[0])
        subanswers = self.letterCombinations(digits[1:])
        if len(subanswers) > 0:
            return [
                firstChar + subans
                for firstChar in self.digitCharMap[firstDigit]
                for subans in subanswers
            ]
        else:
            return [char for char in self.digitCharMap[firstDigit]]


# @lc code=end
