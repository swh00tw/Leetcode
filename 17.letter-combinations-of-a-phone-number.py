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
            9: "wxyz"
        }
    def letterCombinations(self, digits: str) -> List[str]:
        # return all possible result string from digits
        if len(digits)==0:
            return []
        firstDigit = digits[0]
        substrings = self.letterCombinations(digits[1:])
        if len(substrings)==0:
            return list(self.digitCharMap[int(firstDigit)])
        
        res = []
        for startChar in self.digitCharMap[int(firstDigit)]:
            res += [startChar+substring for substring in substrings]
        return res
              
    
        
# @lc code=end

