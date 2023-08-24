#
# @lc app=leetcode id=68 lang=python3
#
# [68] Text Justification
#


# @lc code=start
class SentenceBuilder:
    def __init__(self, maxLength):
        self.words = []
        self.maxLength = maxLength

    def addWord(self, w):
        length = self.getLength()
        if len(self.words) == 0:
            self.words.append(w)
            return True
        if length + 1 + len(w) > self.maxLength:
            return False

        self.words.append(w)
        return True

    def genSentence(self, isLast=False):
        if isLast or len(self.words) == 1:
            tmp = " ".join(self.words)
            return tmp + " " * (self.maxLength - len(tmp))
        if len(self.words) == 2:
            length = self.getLength()
            middle = " " * (self.maxLength - (length - 1))
            return self.words[0] + middle + self.words[1]
        spaces = [1] * (len(self.words) - 1)
        restSpace = self.maxLength - self.getLength()
        idx = 0
        while restSpace > 0:
            spaces[idx] += 1
            restSpace -= 1
            idx = (idx + 1) % (len(spaces))

        ans = ""
        for i in range(len(self.words)):
            if i != 0:
                ans += " " * spaces[i - 1]
            ans += self.words[i]
        return ans

    def reset(self):
        self.words = []

    def getLength(self):
        return len(" ".join(self.words))

    def __repr__(self):
        return f"{self.words}"


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        builder = SentenceBuilder(maxLength=maxWidth)
        for i in range(len(words)):
            res = builder.addWord(words[i])
            if res == False:
                ans.append(builder.genSentence())
                builder.reset()
                builder.addWord(words[i])
        ans.append(builder.genSentence(isLast=True))
        return ans


# @lc code=end
