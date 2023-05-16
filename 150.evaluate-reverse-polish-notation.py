#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
def isOperator(token):
    operators = set(["+", "-", "/", "*"])
    return token in operators

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # create a stack and parse tokens
        # if we encounter a number --> push into stack
        # encounter a operator --> pop top most two number and calculate the result number, push into stack
        s = []
        for t in tokens:
            if isOperator(t):
                n2 = s.pop(-1)
                n1 = s.pop(-1)
                res = 0
                if t == "+":
                    res = n1+n2
                elif t == "-":
                    res = n1-n2
                elif t == "*":
                    res = n1*n2
                else:
                    res = int(n1/n2)
                s.append(res)
            else:
                s.append(int(t))
        return s[0]

        
# @lc code=end

