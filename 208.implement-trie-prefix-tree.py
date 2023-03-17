#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start
class Node:
    def __init__(self, word):
        self.val = word
        self.children = [] # list of Nodes

    def addChild(self, wordNode):
        self.children.append(wordNode)

class Trie:

    def __init__(self):
        # from a to z
        charDict = {} # key: first letter, val: Node[]
        chars = "abcdefghijklmnopqrstuvwxyz"
        for char in chars:
            charDict[char]=None
        self.charDict = charDict

    def insert(self, word: str) -> None:
        print("------------------")
        print("Insert: ", word)
        firstChar = word[0]
        if self.charDict.get(firstChar)==None:
            self.charDict[firstChar] = [Node(word)]
        else:
            x = None
            y = None
            for node in self.charDict[firstChar]:
                if word.startswith(node.val):
                    y = node
                    break
            while True:
                print("node: ", y.val if y!=None else "None")
                if y == None:
                    wordNode = Node(word)
                    # case 1
                    if x == None:
                        self.charDict[firstChar].append(wordNode)
                    # case 2
                    else:
                        x.addChild(wordNode)
                    break
                if y.val.startswith(word):
                    # case 1
                    if x == None:
                        newHead = Node(word)
                        newHead.addChild(y)
                        index = -1
                        for i, node in enumerate(self.charDict[firstChar]):
                            if node.val == y.val:
                                index = i
                                break
                        if index != -1:
                            del self.charDict[firstChar][index]
                        self.charDict[firstChar].append(newHead)
                    # case 2
                    else:
                        wordNode = Node(word)
                        wordNode.addChild(y)
                        # replace
                        index = -1
                        for i, node in enumerate(x.children):
                            if node.val == y.val:
                                index = i
                                break
                        if index != -1:
                            del x.children[index]
                        x.addChild(wordNode)
                    break
                            
                # traverse thru list to find if word is prefixed by any Node
                next = None
                for node in y.children:
                    if word.startswith(node.val):
                        next = node
                        break
                x = y
                y = next

    def search(self, word: str) -> bool:
        print("------------------")
        print("search for ", word)
        firstLetter = word[0]
        if self.charDict.get(firstLetter)==None:
            return False
        else:
            for node in self.charDict[firstLetter]:
                if word == node.val:
                    return True
                
            currNode = None
            for node in self.charDict[firstLetter]:
                if word.startswith(node.val):
                    currNode = node
                    break
            while currNode:
                print("visit... ", currNode.val)
                if currNode.val == word:
                    return True
                next = None
                for node in currNode.children:
                    if word.startswith(node.val):
                        next = node
                        break
                currNode = next
            return False

    def startsWith(self, prefix: str) -> bool:
        print("------------------")
        print("search for prefix ", prefix)
        firstLetter = prefix[0]
        if self.charDict.get(firstLetter)==None:
            return False
        else:
            for node in self.charDict[firstLetter]:
                if node.val.startswith(prefix):
                    return True

            currNode = None
            for node in self.charDict[firstLetter]:
                if prefix.startswith(node.val):
                    currNode = node
                    break
            while currNode:
                print("visit... ", currNode.val)
                if currNode.val.startswith(prefix):
                    return True
                if prefix.startswith(currNode.val):
                    # keep finding
                    for node in currNode.children:
                        if node.val.startswith(prefix):
                            return True
                    next = None
                    for node in currNode.children:
                        if prefix.startswith(node.val):
                            next = node
                    currNode = next    
                else:
                    return False
            return False
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

