#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
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


class WordDictionary:
    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        # only lowercase
        self.trie.insert(word)

    def search(self, word: str) -> bool:
        # can be lowercase and "."
        tree = self.trie.tree

        def match(currDict: dict, word: str) -> bool:
            # base case: if word == ""
            if len(word) == 0:
                return self.trie.end in currDict

            letter = word[0]
            # case 1: letter is not '.'
            if letter != ".":
                if letter not in currDict:
                    return False
                return match(currDict[letter], word[1:])
            # case 2: letter is '.'
            else:
                ansFromChildren = []
                for key in currDict:
                    # ignore the ending character
                    if key == self.trie.end:
                        continue
                    nextDict = currDict[key]
                    ansFromChildren.append(match(nextDict, word[1:]))
                return any(ansFromChildren)

        return match(tree, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end
