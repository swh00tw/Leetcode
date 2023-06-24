#
# @lc app=leetcode id=956 lang=python3
#
# [956] Tallest Billboard
#

# @lc code=start
class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        n = len(rods)
        if n==1:
            return 0
        # create a map dp to map from diff(taller-shorter) to taller(maxHeight)
        dp = {}
        dp[0] = 0
        for r in rods:
            # either not join, join taller, and join shorter
            # no join
            newDp = dp.copy()
            for diff, taller in dp.items():
                shorter = taller - diff
                # add to taller
                newDp[diff+r] = max(newDp.get(diff+r, 0), taller+r)
                # add to shorter
                newDiff = abs(diff-r)
                newTaller = max(taller, shorter+r)
                newDp[newDiff] = max(newDp.get(newDiff, 0), newTaller)
            dp = newDp
        return dp.get(0, 0)

                
        
# @lc code=end

