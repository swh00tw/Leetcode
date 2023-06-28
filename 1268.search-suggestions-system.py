#
# @lc app=leetcode id=1268 lang=python3
#
# [1268] Search Suggestions System
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
            
            if currDict.get("match"):
                currDict["match"].append(word)
            else:
                currDict["match"] = [word]
    def getTree(self):
        return self.tree

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        products = sorted(products) # sorted lexicographically
        for p in products:
            trie.insert(p)
        ans = []
        chars = list(searchWord)
        currDict = trie.getTree()
        while chars:
            char = chars.pop(0)
            if char not in currDict:
                break
            currDict = currDict[char]
            res = currDict["match"][:min(3, len(currDict["match"]))] if "match" in currDict else []
            ans.append(res)
        if len(ans)!=len(searchWord):
            for _ in range(len(searchWord)-len(ans)):
                ans.append([])
        return ans
        
# @lc code=end

