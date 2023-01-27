#
# @lc app=leetcode id=472 lang=python3
#
# [472] Concatenated Words
#

# @lc code=start

# ref: https://leetcode.com/problems/concatenated-words/solutions/3103568/day-27-simple-recursion-dfs-easiest-beginner-friendly-sol/

# KEY: 
# 1. use recursive (I successfully identify this problem must use recursive)
# 2. use Set to reduce time complexity (I only used simple data structure, so I got TLE)

def checkConcatable(word: str, s: set) -> bool:
    for i in range(1, len(word)):
        prefix = word[:i]
        suffix = word[i:]
        if (prefix in s) and (suffix in s or checkConcatable(suffix, s)):
            return True
    return False
    
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # create a word set
        wordSet = set()
        for w in words:
            wordSet.add(w)
        answers = []
        for w in words:
            if (checkConcatable(w, wordSet)):
                answers.append(w)
        return answers
        
# @lc code=end

