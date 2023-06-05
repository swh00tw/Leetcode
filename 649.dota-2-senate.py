#
# @lc app=leetcode id=649 lang=python3
#
# [649] Dota2 Senate
#

# @lc code=start
# ref: https://leetcode.com/problems/dota2-senate/solutions/3483399/simple-diagram-explanation/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r = []
        d = []
        n = len(senate)
        for i, s in enumerate(list(senate)):
            if s== "R":
                r.append(i)
            else:
                d.append(i)
        while r and d:
            rEarliest = r.pop(0)
            dEarliest = d.pop(0)
            if rEarliest < dEarliest:
                r.append(rEarliest+n)
            else:
                d.append(dEarliest+n)
        return "Radiant" if len(d)==0 else "Dire"
        
# @lc code=end

