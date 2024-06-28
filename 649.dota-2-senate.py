#
# @lc app=leetcode id=649 lang=python3
#
# [649] Dota2 Senate
#

from collections import deque


# @lc code=start
# ref: https://leetcode.com/problems/dota2-senate/solutions/3483399/simple-diagram-explanation/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # maintain a queue
        # first put 'R' or 'D' into queue in order
        # then pop the first guy, he/she can use the power to ban one enemy, and add back to the queue
        # in other word, the enemy behind need to be pop and skip
        # if the queue only contains people from one party, they win
        total_r = 0
        n = len(senate)
        for c in senate:
            if c == "R":
                total_r += 1
        total_d = n - total_r

        skip_r = 0
        skip_d = 0
        queue = deque(list(senate))
        while queue:
            rOrd = queue.popleft()
            if rOrd == "R":
                if skip_r > 0:
                    skip_r -= 1
                    total_r -= 1
                else:
                    skip_d += 1
                    queue.append(rOrd)
            else:
                if skip_d > 0:
                    skip_d -= 1
                    total_d -= 1
                else:
                    skip_r += 1
                    queue.append(rOrd)
            if total_d == 0:
                return "Radiant"
            elif total_r == 0:
                return "Dire"


# @lc code=end
