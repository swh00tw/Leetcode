#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#

# @lc code=start
from typing import Union, List, Tuple


class Element:
    def __init__(self, num: int, child: str):
        self.num = num
        self.child = child

    def stringify(self) -> str:
        elementOrStrs = self.divideChild()
        res = ""
        for elementOrStr in elementOrStrs:
            if isinstance(elementOrStr, Element):
                res += elementOrStr.stringify()
            else:
                res += elementOrStr
        return res * self.num

    def divideChild(self) -> List[Union["Element", str]]:
        # '3[a]2[bc]' --> ['3[a]', '2[bc]']
        substrings = []
        left = 0
        right = 0
        start = 0
        for i, c in enumerate(self.child):
            if c == "[":
                left += 1
            elif c == "]":
                right += 1
            if left == right and not c.isdigit():
                substrings.append(self.child[start : i + 1])
                start = i + 1
        if start < len(self.child):
            substrings.append(self.child[start:])
        elements = []
        for e in substrings:
            if self.isElement(e):
                num, child = self.getNumAndChild(e)
                elements.append(Element(num, child))
            else:
                elements.append(e)
        return elements

    def isElement(self, string) -> bool:
        if len(string) == 0:
            return False
        return string[0].isdigit()

    def getNumAndChild(self, elementStr) -> Tuple[int, str]:
        num = ""
        for i, c in enumerate(elementStr):
            if c.isdigit():
                num += c
            else:
                return (int(num), elementStr[i + 1 : -1])


class Solution:
    def decodeString(self, s: str) -> str:
        root = Element(1, s)
        return root.stringify()


# @lc code=end
