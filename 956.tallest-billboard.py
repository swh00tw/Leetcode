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
        # create an dp array that store a map
        # it map from "diff" of two sets and the maximum height of two sides
        # for each new rod, it can whether not join any set or join one side of two sets
        dp = [{} for _ in range(n)]
        dp[0][rods[0]] = rods[0]
        dp[0][0] = 0
        for i in range(1, n):
            newRod = rods[i]
            # not join any side
            dp[i] = dp[i-1].copy()
            for diff in dp[i-1]:
                # join larger
                maxH = dp[i-1][diff]
                dp[i][diff+newRod] = max(maxH+newRod, dp[i].get(diff+newRod, 0))
                # join smaller
                if diff >= newRod:
                    dp[i][diff - newRod] = max(maxH, dp[i].get(diff - newRod, 0))
                else:
                    dp[i][newRod - diff] = max(maxH + newRod - diff, dp[i].get(newRod - diff, 0))
        return dp[-1].get(0, 0)

                
        
# @lc code=end

