#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start
from collections import deque


class Trie:
    def __init__(self):
        self.tree = {}
        self.end = "#"  # use this character to indicate the end of a word

    def insert(self, word: str) -> None:
        currDict = self.tree
        w = deque(list(word))
        while w:
            letter = w.popleft()
            if letter not in currDict:
                currDict[letter] = {}
            currDict = currDict[letter]
        currDict[self.end] = True

    def search(self, word: str) -> bool:
        # recursive traverse through the tree along the path built by letters
        # if in the end, we reach "#", return True else False
        w = deque(list(word))
        currDict = self.tree
        while w:
            letter = w.popleft()
            if letter not in currDict:
                return False
            currDict = currDict[letter]
        return self.end in currDict

    def startsWith(self, prefix: str) -> bool:
        # recursive traverse through the tree along the path built by letters
        # if in the end, we reach "#", return True else False
        w = deque(list(prefix))
        currDict = self.tree
        while w:
            letter = w.popleft()
            if letter not in currDict:
                return False
            currDict = currDict[letter]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end
