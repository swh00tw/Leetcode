#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#

# @lc code=start
from collections import deque


class Trie:
    def __init__(self):
        self.tree = {}
        self.end = "/"

    def insert(self, word):
        w = deque(list(word))
        currDict = self.tree
        while w:
            letter = w.popleft()
            if letter not in currDict:
                currDict[letter] = {}
            currDict = currDict[letter]
        currDict[self.end] = word

    def search(self, word) -> bool:
        w = deque(list(word))
        currDict = self.tree
        while w:
            letter = w.popleft()
            if letter not in currDict:
                return False
            currDict = currDict[letter]
        return self.end in currDict

    def startwith(self, word) -> bool:
        w = deque(list(word))
        currDict = self.tree
        while w:
            letter = w.popleft()
            if letter not in currDict:
                return False
            currDict = currDict[letter]
        return True


# ref: https://leetcode.com/problems/word-search-ii/solutions/2779919/python-trie-easy-solution/
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # first, build trie and insert all the words into trie
        # trie should support insert, search, startwith
        ans = set()
        deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m = len(board)
        n = len(board[0])
        trie = Trie()
        for w in words:
            trie.insert(w)

        def dfs(position, currDict) -> List[str]:
            x, y = position
            new_char = board[x][y]
            next_dict = currDict.get(new_char, None)
            if next_dict is None:
                return

            # if we find "/" in next_dict, it means we found
            if "/" in next_dict:
                ans.add(next_dict["/"])

            board[x][y] = "#"  # mask that position to prevent backward propagation
            for dx, dy in deltas:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    dfs((nx, ny), next_dict)
            board[x][y] = new_char  # recover back

        for i in range(m):
            for j in range(n):
                dfs((i, j), trie.tree)
        return list(ans)


# @lc code=end
