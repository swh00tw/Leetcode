#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start
class Trie:

    def __init__(self):
        self.tree = {}

    def insert(self, word: str) -> None:
        chars = list(word)
        currDict = self.tree
        while chars:
            char = chars.pop(0)
            if not currDict.get(char):
                currDict[char] = {}
            currDict = currDict[char]
        currDict["/"] = True

    def search(self, word: str) -> bool:
        chars = list(word)
        currDict = self.tree
        while chars:
            char = chars.pop(0)
            if char not in currDict:
                return False
            currDict = currDict[char]
        return "/" in currDict

    def startsWith(self, prefix: str) -> bool:
        chars = list(prefix)
        currDict = self.tree
        while chars:
            char = chars.pop(0)
            if char not in currDict:
                return False
            currDict = currDict[char]
        return True

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

