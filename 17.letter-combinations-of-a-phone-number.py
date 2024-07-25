#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#


# @lc code=start
class Solution:
    def __init__(self):
        self.map = {
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
        # recursive
        # edge case: len(digits) == 0: return []
        # get the first digit in digits,
        # append the possible first letter for all combination in letterCombinations(digits[1:])
        if len(digits) == 0:
            return []
        allCombinations = self.letterCombinations(digits[1:])
        key = int(digits[0])
        if not allCombinations:
            return list(self.map[key])
        return [
            letter + comb for letter in list(self.map[key]) for comb in allCombinations
        ]


# @lc code=end
