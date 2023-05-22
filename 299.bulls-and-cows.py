#
# @lc app=leetcode id=299 lang=python3
#
# [299] Bulls and Cows
#

# @lc code=start
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        n = len(secret)
        indices = []
        bulls = 0
        # count bulls
        for i in range(n):
            if secret[i]==guess[i]:
                bulls+=1
            else:
                indices.append(i)
        d = {}
        for i in indices:
            d[secret[i]]=1+d.get(secret[i], 0)
        cows = 0
        for i in indices:
            if guess[i] in d and d[guess[i]]>0:
                cows+=1
                d[guess[i]]-=1
        return f"{bulls}A{cows}B"

        
# @lc code=end

